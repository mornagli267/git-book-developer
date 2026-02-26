#!/usr/bin/env python3
"""
fix_attachment_links.py  (v2 — fixed)

Finds all markdown links like:
    [filename.pdf](attachments/filename.pdf)

And converts them based on file type:
    - Images (.png, .jpg, .gif, .svg, .webp) → ![alt](../.gitbook/assets/file.png)
    - Supported files (.pdf, .zip, .xlsx, etc.) → {% file src="../.gitbook/assets/file.pdf" %}
    - Unsupported files (.exe, .BIN, .signed) → SKIPPED (left as plain links)

Also copies the actual files from attachments/ into .gitbook/assets/.

SAFE BY DEFAULT:
    python fix_attachment_links.py            → DRY RUN (shows changes, touches nothing)
    python fix_attachment_links.py --apply    → APPLIES changes (modifies files)

Run from the root of your git-book-developer repo.
"""

import os
import re
import sys
import shutil
from urllib.parse import unquote

# ─── CONFIG ──────────────────────────────────────────────────────────
GITBOOK_ASSETS = ".gitbook/assets"

# Extensions GitBook accepts in {% file %} blocks (from actual allowed MIME types)
GITBOOK_FILE_EXTENSIONS = {
    ".zip", ".pdf", ".xlsx", ".xls", ".csv",
    ".md", ".html", ".htm",
    ".docx", ".doc",
    ".rar",
    ".gz", ".tar", ".tgz",
    ".dxf", ".step", ".stp",
}

# Image extensions → use ![alt]() syntax instead of {% file %}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}

# Extensions that GitBook blocks (won't parse in {% file %})
BLOCKED_EXTENSIONS = {".exe", ".bin", ".msi", ".bat", ".cmd", ".sh", ".signed"}

# Files renamed in .gitbook/assets/ (old attachment name → actual asset name)
# Parentheses break GitBook's {% file %} parser, so these were renamed
RENAME_MAP = {
    "Quectel_Windows_USB_Driver(Q)_NDIS_V2.2.exe": "Quectel_Windows_USB_Driver_Q_NDIS_V2.2.exe",
    "Quectel_Windows_USB_Driver(Q)_RNDIS_V1.1.4.zip": "Quectel_Windows_USB_Driver_Q_RNDIS_V1.1.4.zip",
}
# ─────────────────────────────────────────────────────────────────────

APPLY_MODE = "--apply" in sys.argv


def find_attachment_links(line):
    """
    Find all [text](attachments/path) links in a line.
    Handles parentheses in filenames by matching balanced parens.
    """
    matches = []
    i = 0
    while i < len(line):
        # Find start of markdown link: [
        if line[i] != '[':
            i += 1
            continue

        # Find the link text between [ and ]
        bracket_start = i
        i += 1
        bracket_depth = 1
        while i < len(line) and bracket_depth > 0:
            if line[i] == '[':
                bracket_depth += 1
            elif line[i] == ']':
                bracket_depth -= 1
            i += 1

        if bracket_depth != 0:
            continue

        bracket_end = i - 1  # position of closing ]
        link_text = line[bracket_start + 1:bracket_end]

        # Expect ( immediately after ]
        if i >= len(line) or line[i] != '(':
            continue

        # Find matching ) — handle nested parens in filename
        paren_start = i
        i += 1
        paren_depth = 1
        while i < len(line) and paren_depth > 0:
            if line[i] == '(':
                paren_depth += 1
            elif line[i] == ')':
                paren_depth -= 1
            i += 1

        if paren_depth != 0:
            continue

        paren_end = i - 1  # position of closing )
        link_target = line[paren_start + 1:paren_end]

        # Check if this is an attachment link
        decoded_target = unquote(link_target)
        if not re.match(r'\.?/?attachments/', decoded_target):
            continue

        full_match = line[bracket_start:paren_end + 1]
        matches.append({
            "full_match": full_match,
            "link_text": link_text,
            "link_target": link_target,
            "decoded_target": decoded_target,
        })

    return matches


def relative_gitbook_path(md_file_path):
    """Relative path from a .md file's directory to .gitbook/assets/"""
    md_dir = os.path.dirname(md_file_path)
    rel = os.path.relpath(GITBOOK_ASSETS, md_dir)
    return rel.replace("\\", "/")


def decode_filename(encoded_path):
    """Decode URL-encoded filename: %20 → space, etc."""
    return unquote(os.path.basename(encoded_path))


def get_file_ext(filename):
    """Get lowercase file extension."""
    return os.path.splitext(filename)[1].lower()


def classify_file(filename):
    """
    Classify how a file should be handled:
      'image'   → ![alt]() syntax
      'file'    → {% file %} syntax
      'skip'    → leave as plain markdown link (unsupported by GitBook)
      'unknown' → not in any known list, skip to be safe
    """
    ext = get_file_ext(filename)
    if ext in IMAGE_EXTENSIONS:
        return "image"
    if ext in BLOCKED_EXTENSIONS:
        return "skip"
    if ext in GITBOOK_FILE_EXTENSIONS:
        return "file"
    # Unknown extension — skip to be safe
    return "unknown"


def make_replacement(classification, rel_path, filename, link_text):
    """Generate the replacement syntax based on file classification."""
    asset_path = "{}/{}".format(rel_path, filename)

    if classification == "image":
        alt = link_text if link_text else filename
        return '![{}]({})'.format(alt, asset_path)
    elif classification == "file":
        return '{{% file src="{}" %}}'.format(asset_path)
    else:
        return None  # skip / unknown — no replacement


def main():
    # ─── Banner ──────────────────────────────────────────────────────
    print()
    print("=" * 70)
    if APPLY_MODE:
        print("  ⚡ APPLY MODE — files WILL be modified and copied")
        print("     Make sure you have a clean git state (git stash / commit first)")
    else:
        print("  🔍 DRY RUN — scanning only, nothing will be changed")
        print("     Add --apply to actually make changes")
    print("=" * 70)
    print()

    if not os.path.exists("SUMMARY.md"):
        print("  ❌ SUMMARY.md not found. Are you in the repo root?")
        sys.exit(1)

    # ─── Scan ────────────────────────────────────────────────────────
    total_links = 0
    total_files = 0
    skipped_links = 0
    copy_tasks = []      # (source_path, dest_path)
    missing_src = []     # source files that don't exist
    all_changes = []     # (md_path, original_text, replacement_text)

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in (".git",)]

        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue

            md_path = os.path.join(root, fname)

            try:
                with open(md_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except (UnicodeDecodeError, PermissionError):
                continue

            lines = content.split("\n")
            file_matches = []

            for line_idx, line in enumerate(lines):
                for match in find_attachment_links(line):
                    link_text = match["link_text"]
                    link_target = match["link_target"]
                    full_match_str = match["full_match"]
                    decoded_target = match["decoded_target"]

                    filename = decode_filename(decoded_target)

                    # Apply rename map (e.g. parens → underscores)
                    asset_filename = RENAME_MAP.get(filename, filename)

                    # Classify the file based on the ASSET filename
                    classification = classify_file(asset_filename)

                    # Where the file currently lives
                    md_dir = os.path.dirname(md_path)
                    src_full = os.path.normpath(
                        os.path.join(md_dir, decoded_target)
                    )

                    # Where it should go (use asset_filename for destination)
                    dest_full = os.path.join(GITBOOK_ASSETS, asset_filename)

                    # New syntax (use asset_filename)
                    rel_path = relative_gitbook_path(md_path)
                    new_syntax = make_replacement(classification, rel_path, asset_filename, link_text)

                    # Check file existence
                    src_exists = os.path.exists(src_full)
                    dest_exists = os.path.exists(dest_full)

                    if classification in ("skip", "unknown"):
                        file_status = "⏭️  SKIP ({})".format(classification)
                        skipped_links += 1
                    elif src_exists and not dest_exists:
                        copy_tasks.append((src_full, dest_full))
                        file_status = "📦 COPY"
                    elif dest_exists:
                        file_status = "✅ EXISTS in assets"
                    else:
                        missing_src.append(src_full)
                        file_status = "⚠️  NOT FOUND"

                    type_label = {
                        "image": "🖼️  IMAGE",
                        "file": "📄 FILE",
                        "skip": "🚫 BLOCKED",
                        "unknown": "❓ UNKNOWN",
                    }.get(classification, "?")

                    rename_note = ""
                    if asset_filename != filename:
                        rename_note = " (renamed → {})".format(asset_filename)

                    file_matches.append({
                        "line": line_idx + 1,
                        "old": full_match_str,
                        "new": new_syntax or "(no change)",
                        "status": file_status,
                        "filename": filename + rename_note,
                        "type_label": type_label,
                        "classification": classification,
                    })

                    if new_syntax:
                        all_changes.append((md_path, full_match_str, new_syntax))

            # Print file results
            if file_matches:
                total_files += 1
                total_links += len(file_matches)
                print("📄 {}".format(md_path))
                for m in file_matches:
                    print("   Line {:>4}  [{}]  [{}]  {}".format(
                        m["line"], m["status"], m["type_label"], m["filename"]
                    ))
                    print("        OLD → {}".format(m["old"]))
                    print("        NEW → {}".format(m["new"]))
                print()

    # ─── Summary ─────────────────────────────────────────────────────
    print("=" * 70)
    print("  SCAN RESULTS")
    print("=" * 70)
    print("  Attachment links found:   {}".format(total_links))
    print("  Will convert:             {}".format(len(all_changes)))
    print("  Skipped (unsupported):    {}".format(skipped_links))
    print("  Markdown files affected:  {}".format(total_files))
    print("  Files to copy to assets:  {}".format(len(copy_tasks)))
    print("  Missing source files:     {}".format(len(missing_src)))
    print()

    if missing_src:
        print("  ⚠️  MISSING — these files were referenced but not found:")
        for mf in sorted(set(missing_src)):
            print("     {}".format(mf))
        print()
        print("  (These may already be in .gitbook/assets/ under a different")
        print("   name, or they might have been deleted. Check manually.)")
        print()

    if len(all_changes) == 0:
        print("  ✅ Nothing to fix!")
        return

    # ─── Dry run exit ────────────────────────────────────────────────
    if not APPLY_MODE:
        print("─" * 70)
        print("  This was a DRY RUN. To apply these changes, run:")
        print()
        print("    python fix_attachment_links.py --apply")
        print()
        print("  Recommended workflow:")
        print("    1. git status          (make sure working tree is clean)")
        print("    2. python fix_attachment_links.py --apply")
        print("    3. git diff            (review all changes)")
        print("    4. git add -A && git commit -m 'fix: attachment links'")
        print("    5. git push            (GitBook will sync)")
        print("─" * 70)
        return

    # ─── Confirm before proceeding ───────────────────────────────────
    print("─" * 70)
    print("  About to convert {} links and copy {} assets.".format(
        len(all_changes), len(copy_tasks)
    ))
    print("  Skipping {} unsupported links (will remain as plain markdown).".format(
        skipped_links
    ))
    print()
    confirm = input("  Type 'yes' to proceed: ").strip().lower()
    if confirm != "yes":
        print("\n  ❌ Aborted. No changes made.")
        return
    print()

    # ─── Copy files to .gitbook/assets/ ──────────────────────────────
    os.makedirs(GITBOOK_ASSETS, exist_ok=True)
    copied = 0
    for src, dst in copy_tasks:
        if os.path.exists(src):
            shutil.copy2(src, dst)
            copied += 1
            print("  📦 Copied: {} → {}".format(os.path.basename(src), dst))

    if copied:
        print()

    # ─── Update markdown files ───────────────────────────────────────
    changes_by_file = {}
    for md_path, old, new in all_changes:
        changes_by_file.setdefault(md_path, []).append((old, new))

    updated = 0
    for md_path, replacements in changes_by_file.items():
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        for old, new in replacements:
            content = content.replace(old, new)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(content)

        updated += 1
        print("  ✏️  Updated: {}".format(md_path))

    print()
    print("=" * 70)
    print("  ✅ DONE")
    print("=" * 70)
    print("  Markdown files updated:  {}".format(updated))
    print("  Assets copied:           {}".format(copied))
    print("  Links skipped:           {}".format(skipped_links))
    print()
    print("  NEXT STEPS:")
    print("    1. git diff                (review every change carefully)")
    print("    2. git add -A")
    print("    3. git commit -m 'fix: convert attachment links to gitbook syntax'")
    print("    4. git push")
    print("    5. Verify on your GitBook site after sync")
    print()


if __name__ == "__main__":
    main()
