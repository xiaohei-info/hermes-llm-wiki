from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'README.md',
    'AGENTS.md',
    'SOUL.md',
    'MEMORY.md',
    'docs/implementation-guide.md',
    'skills/README.md',
    'templates/cron/README.md',
]

MARKDOWN_EXTS = {'.md'}
LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')

missing = [p for p in REQUIRED_FILES if not (ROOT / p).exists()]
if missing:
    print('Missing required files:')
    for item in missing:
        print(f'  - {item}')
    sys.exit(1)

errors = []
for md_file in ROOT.rglob('*.md'):
    text = md_file.read_text(encoding='utf-8')
    for target in LINK_RE.findall(text):
        if target.startswith('http://') or target.startswith('https://') or target.startswith('#'):
            continue
        normalized = target.split('#', 1)[0]
        if not normalized:
            continue
        candidate = (md_file.parent / normalized).resolve()
        if not candidate.exists():
            errors.append(f'{md_file.relative_to(ROOT)} -> missing link target: {target}')

if errors:
    print('Broken relative markdown links found:')
    for err in errors:
        print(f'  - {err}')
    sys.exit(1)

print('Repo validation passed.')
