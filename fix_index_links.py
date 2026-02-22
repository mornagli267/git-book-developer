#!/usr/bin/env python3
"""
Fix doubled paths in vendor index pages.

E.g. in marvell/cn913x.md:
  (marvell/cn913x/com-som.md) → (cn913x/com-som.md)
  (marvell/cn913x/sbc-platform.md) → (cn913x/sbc-platform.md)
"""

import os
import re
import sys

DRY_RUN = '--dry-run' in sys.argv

# Files to fix: (filepath, wrong_prefix)
# Each file is at vendor/product.md and links start with vendor/product/...
# They should start with just product/...
files = [
    ('marvell/cn913x.md', 'marvell/'),
    ('marvell/a8040.md', 'marvell/'),
    ('nxp/imx8.md', 'nxp/'),
    ('nxp/imx6.md', 'nxp/'),
    ('nxp/lx2160a.md', 'nxp/'),
    ('nxp/lx2162a.md', 'nxp/'),
    ('amd/v3000.md', 'amd/'),
    ('amd/r8000-r7000.md', 'amd/'),
    ('ti/am64x.md', 'ti/'),
    ('renesas/rz-v2n.md', 'renesas/'),
    ('renesas/rz-g2ul-g2lc.md', 'renesas/'),
    ('renesas/rz-g2l-v2l.md', 'renesas/'),
    ('intel/braswell.md', 'intel/'),
    ('hailo/hailo-15.md', 'hailo/'),
]

fixed = 0
for filepath, prefix in files:
    if not os.path.exists(filepath):
        print(f'  SKIP (not found): {filepath}')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    # Replace (prefix + path) with just (path) in markdown links
    # Matches: (marvell/cn913x/com-som.md) → (cn913x/com-som.md)
    # Matches: (marvell/cn913x/sbc-platform.md) → (cn913x/sbc-platform.md)
    content = re.sub(
        r'\(' + re.escape(prefix) + r'([^)]+(?:com-som|sbc-platform)[^)]*)\)',
        r'(\1)',
        content
    )

    if content != original:
        if DRY_RUN:
            print(f'  WOULD FIX: {filepath}')
        else:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  FIXED: {filepath}')
        fixed += 1
    else:
        print(f'  NO CHANGE: {filepath}')

print(f'\n{fixed} files {"would be " if DRY_RUN else ""}fixed')
