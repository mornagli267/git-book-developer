#!/usr/bin/env python3
"""
Convert remaining standalone/bullet attachment links to {% file %} blocks.
Phase 4 only caught '* [name](path)' bullets. This catches:
- Standalone lines: [name](attachments/file.ext)
- Dash bullets: - [name](attachments/file.ext)
Leaves inline links (text before/after the link on same line) untouched.
"""

import os
import re
import sys

DRY_RUN = '--dry-run' in sys.argv

ATTACHMENT_EXTS = (
    '.pdf', '.zip', '.xlsx', '.rar', '.dxf', '.step',
    '.rom', '.signed', '.gz', '.bin', '.img', '.patch',
)

def is_attachment_link(path):
    """Check if path points to an attachment file."""
    lower = path.lower()
    # Must contain 'attachments/' in path
    if 'attachments/' not in lower and 'attachments%2f' not in lower:
        return False
    return any(lower.endswith(ext) for ext in ATTACHMENT_EXTS)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    changes = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Skip lines inside tables (contain | at start and end)
        if stripped.startswith('|') and stripped.endswith('|'):
            new_lines.append(line)
            continue

        # Pattern: standalone link on its own line (possibly with - or * bullet)
        # Match: optional whitespace, optional bullet (- or *), then [text](path)
        m = re.match(r'^(\s*(?:[-*]\s+)?)\[([^\]]+)\]\(([^)]+)\)\s*$', stripped)
        if m:
            prefix_ws = ''  # We'll use original indentation
            link_text = m.group(2)
            link_path = m.group(3)

            if is_attachment_link(link_path):
                new_line = '{%% file src="%s" %%}\n' % link_path
                changes.append((i + 1, stripped.strip(), new_line.strip()))
                new_lines.append(new_line)
                continue

        # Check for multiple links on one line that are ALL attachment links
        # e.g.: [file1](path1) [file2](path2) [file3](path3)
        all_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', stripped)
        if len(all_links) > 1:
            # Check if ALL are attachment links and line is ONLY links
            reconstructed = ' '.join(f'[{t}]({p})' for t, p in all_links)
            if stripped == reconstructed and all(is_attachment_link(p) for _, p in all_links):
                result = ''
                for text, path in all_links:
                    result += '{%% file src="%s" %%}\n' % path
                changes.append((i + 1, stripped, result.strip()))
                new_lines.append(result)
                continue

        # Leave everything else untouched
        new_lines.append(line)

    return new_lines, changes

def main():
    if not os.path.exists('SUMMARY.md'):
        print("ERROR: Run from the git-book-developer root directory")
        sys.exit(1)

    if DRY_RUN:
        print("=== DRY RUN MODE ===\n")

    total_fixes = 0
    total_files = 0

    for dirpath, dirnames, filenames in os.walk('.'):
        dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules')]
        for fname in filenames:
            if not fname.endswith('.md'):
                continue
            filepath = os.path.join(dirpath, fname)
            new_lines, changes = process_file(filepath)

            if changes:
                total_files += 1
                total_fixes += len(changes)
                if DRY_RUN:
                    print(f"  {filepath}:")
                    for lineno, old, new in changes:
                        print(f"    L{lineno} OLD: {old}")
                        print(f"    L{lineno} NEW: {new}")
                else:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                    print(f"  MODIFIED: {filepath} ({len(changes)} links)")

    print(f"\n=== Results ===")
    print(f"Files modified: {total_files}")
    print(f"Links converted: {total_fixes}")

if __name__ == '__main__':
    main()
