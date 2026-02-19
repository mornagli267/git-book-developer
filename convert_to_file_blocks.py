#!/usr/bin/env python3
"""
Convert attachment bullet links to GitBook {% file %} blocks.

Converts:
  * [filename.pdf](path/to/file.pdf)
To:
  {% file src="path/to/file.pdf" %}

Only converts links to attachment file types (pdf, zip, xlsx, rar, dxf, step, etc).
Leaves inline links (mid-sentence) untouched.
"""

import os
import re
import sys

DRY_RUN = '--dry-run' in sys.argv

# File extensions that should become {% file %} blocks
ATTACHMENT_EXTENSIONS = {
    '.pdf', '.zip', '.xlsx', '.xls', '.rar', '.dxf', '.step',
    '.stp', '.dwg', '.csv', '.doc', '.docx', '.ppt', '.pptx',
    '.7z', '.gz', '.tar', '.bz2',
}

def is_attachment_link(path):
    """Check if a link path points to an attachment file."""
    # Remove URL encoding for extension check
    clean = path.split('?')[0]  # remove query params
    _, ext = os.path.splitext(clean.lower())
    return ext in ATTACHMENT_EXTENSIONS

def process_file(filepath, stats):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    modified = False
    
    for line in lines:
        # Match: * [display text](path/to/file.ext)
        # Only match lines that are JUST a bullet link (not inline in text)
        m = re.match(r'^\s*\*\s+\[([^\]]+)\]\(([^)]+)\)\s*$', line)
        if m:
            display_name = m.group(1)
            link_path = m.group(2)
            
            if is_attachment_link(link_path):
                new_lines.append('{%% file src="%s" %%}' % link_path)
                stats['converted'] += 1
                modified = True
                continue
        
        new_lines.append(line)
    
    if modified:
        new_content = '\n'.join(new_lines)
        if DRY_RUN:
            print(f'  WOULD MODIFY: {filepath} ({stats["converted"]} links)')
        else:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'  MODIFIED: {filepath}')
        return True
    return False


def main():
    root = '.'
    if not os.path.exists('SUMMARY.md'):
        print("ERROR: Run from the git-book-developer root directory")
        sys.exit(1)
    
    if DRY_RUN:
        print("=== DRY RUN MODE ===\n")
    
    # Find all .md files that have bullet attachment links
    target_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != '.git']
        for fname in filenames:
            if fname.endswith('.md'):
                full = os.path.join(dirpath, fname)
                with open(full, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Look for bullet links to attachment files
                if re.search(r'^\s*\*\s+\[[^\]]+\]\([^)]+\.(pdf|zip|xlsx|rar|dxf|step)\)', content, re.MULTILINE | re.IGNORECASE):
                    target_files.append(full)
    
    print(f"Found {len(target_files)} files with attachment bullet links\n")
    
    total_stats = {
        'converted': 0,
        'files_modified': 0,
    }
    
    for filepath in sorted(target_files):
        file_stats = {'converted': 0}
        if process_file(filepath, file_stats):
            total_stats['files_modified'] += 1
            total_stats['converted'] += file_stats['converted']
    
    print(f"\n=== Results ===")
    print(f"Files modified:  {total_stats['files_modified']}")
    print(f"Links converted: {total_stats['converted']}")
    
    # Verify: check for any remaining bullet attachment links
    print("\n=== Remaining bullet attachment links ===")
    remaining = 0
    for filepath in sorted(target_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            for lineno, line in enumerate(f, 1):
                if re.match(r'^\s*\*\s+\[[^\]]+\]\([^)]+\.(pdf|zip|xlsx|rar|dxf|step)\)', line, re.IGNORECASE):
                    print(f"  {filepath}:{lineno}: {line.strip()[:120]}")
                    remaining += 1
    if remaining == 0:
        print("  None! All converted.")
    else:
        print(f"  {remaining} remaining")

if __name__ == '__main__':
    main()
