#!/usr/bin/env python3
"""
Fix Confluence links - Convert external Confluence URLs to local GitBook paths.

This script:
1. Builds a mapping of page titles to local file paths
2. Finds all Confluence URLs in markdown files
3. Replaces them with relative local paths
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote

def build_file_index(base_dir):
    """Build index of all .md files with their titles."""
    index = {}
    
    for md_file in Path(base_dir).rglob('*.md'):
        if 'backups' in str(md_file):
            continue
            
        # Get filename without extension as key
        filename = md_file.stem.lower()
        
        # Also try to get title from H1
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read(500)  # Read first 500 chars
                match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                if match:
                    title = match.group(1).strip().lower()
                    # Normalize title
                    title_normalized = re.sub(r'[^a-z0-9]+', '-', title).strip('-')
                    index[title_normalized] = str(md_file)
        except:
            pass
        
        # Index by filename
        index[filename] = str(md_file)
        
        # Also index by filename with common variations
        filename_clean = filename.replace('-', ' ').replace('_', ' ')
        index[filename_clean] = str(md_file)
    
    return index

def extract_page_name_from_url(url):
    """Extract page name from Confluence URL."""
    # Pattern 1: .../pages/123456/Page+Name
    match = re.search(r'/pages/\d+/([^#?\s]+)', url)
    if match:
        page_name = unquote(match.group(1).replace('+', ' '))
        return page_name
    
    # Pattern 2: Just page ID
    match = re.search(r'/pages/(\d+)(?:[#?\s]|$)', url)
    if match:
        return None  # Can't determine from ID alone
    
    return None

def find_local_file(page_name, file_index, current_file):
    """Find local file matching the page name."""
    if not page_name:
        return None
    
    # Normalize page name
    normalized = re.sub(r'[^a-z0-9]+', '-', page_name.lower()).strip('-')
    
    # Direct match
    if normalized in file_index:
        return file_index[normalized]
    
    # Try partial match
    for key, path in file_index.items():
        if normalized in key or key in normalized:
            return path
    
    return None

def get_relative_path(from_file, to_file):
    """Calculate relative path from one file to another."""
    from_path = Path(from_file).parent
    to_path = Path(to_file)
    
    try:
        rel_path = os.path.relpath(to_path, from_path)
        return rel_path
    except:
        return None

def process_file(filepath, file_index, dry_run=False):
    """Process a single file and fix Confluence links."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find all Confluence URLs
    confluence_pattern = r'\[([^\]]+)\]\((https://(?:solidrun\.atlassian\.net|developer\.resources\.solid-run\.com)/wiki/spaces/developer/pages/[^)\s]+)\)'
    
    matches = re.findall(confluence_pattern, content)
    
    changes = []
    for link_text, url in matches:
        page_name = extract_page_name_from_url(url)
        if page_name:
            local_file = find_local_file(page_name, file_index, filepath)
            if local_file:
                rel_path = get_relative_path(filepath, local_file)
                if rel_path:
                    # Handle anchor links
                    anchor = ''
                    if '#' in url:
                        anchor = '#' + url.split('#')[1].split(')')[0].lower().replace('+', '-')
                    
                    old_link = f'[{link_text}]({url})'
                    new_link = f'[{link_text}]({rel_path}{anchor})'
                    content = content.replace(old_link, new_link)
                    changes.append((link_text, url, rel_path + anchor))
    
    if changes and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

def main():
    import sys
    
    base_dir = '.'
    dry_run = '--dry-run' in sys.argv
    
    print("🔍 Building file index...")
    file_index = build_file_index(base_dir)
    print(f"   Found {len(file_index)} indexed pages")
    
    print("\n🔗 Finding Confluence links...")
    
    # Find files with Confluence links
    confluence_pattern = r'solidrun\.atlassian\.net|developer\.resources\.solid-run\.com/wiki'
    
    files_to_process = []
    for md_file in Path(base_dir).rglob('*.md'):
        if 'backups' in str(md_file):
            continue
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Skip files with only macro JS content
                if re.search(confluence_pattern, content) and 'addon_key' not in content[:1000]:
                    files_to_process.append(str(md_file))
        except:
            pass
    
    print(f"   Found {len(files_to_process)} files with Confluence links")
    
    if dry_run:
        print("\n🔍 DRY RUN - No changes will be made\n")
    
    total_fixed = 0
    total_unfixed = 0
    unfixed_urls = []
    
    for filepath in sorted(files_to_process):
        changes = process_file(filepath, file_index, dry_run)
        if changes:
            print(f"\n📄 {filepath}")
            for link_text, old_url, new_path in changes:
                print(f"   ✅ [{link_text}] → {new_path}")
                total_fixed += 1
    
    # Find unfixed links
    print("\n" + "="*60)
    print(f"✅ Fixed: {total_fixed} links")
    
    if not dry_run:
        print("\n🎉 Done! Run 'git diff' to review changes.")
        print("Then: git add . && git commit -m 'Fix Confluence links to local paths' && git push")

if __name__ == '__main__':
    main()
