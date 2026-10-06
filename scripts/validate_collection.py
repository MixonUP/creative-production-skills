"""Read-only structural and content-hash check. Does not execute skill code."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'collection-manifest.json').read_text(encoding='utf-8'))
catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
errors = []
expected = {row['path']: row for row in manifest['files']}
actual = {p.relative_to(root).as_posix(): p for p in (root / 'skills').rglob('*') if p.is_file()}
if expected.keys() != actual.keys():
    errors.append({'file_set_difference': sorted(expected.keys() ^ actual.keys())})
for rel, p in actual.items():
    row = expected.get(rel)
    if row and hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        errors.append({'hash_mismatch': rel})
    if p.name == '.env' or p.suffix in {'.pem', '.key', '.p12', '.pyc', '.db'} or '__pycache__' in p.parts:
        errors.append({'unexpected_sensitive_or_generated_path': rel})
skills = sorted(p.parent.name for p in (root / 'skills').glob('*/SKILL.md'))
catalog_names = sorted(s['name'] for group in catalog for s in group['skills'])
if len(skills) != manifest['skill_count'] or skills != catalog_names or len(set(skills)) != len(skills):
    errors.append({'skill_catalog_mismatch': True})
for name in skills:
    text = (root / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8-sig')
    fm = text.split('---', 2)
    if len(fm) != 3 or not re.search(r'^name:\s*[\"\']?' + re.escape(name) + r'[\"\']?\s*$', fm[1], re.M):
        errors.append({'frontmatter_name_mismatch': name})
    if len(fm) == 3 and not re.search(r'^description:\s*\S', fm[1], re.M):
        errors.append({'missing_description': name})
for required in ['README.md','THIRD_PARTY_NOTICES.md','docs/SKILL_MAP_RU.md','docs/CATALOG_RU.md','docs/SKILL_SOURCES_RU.md','docs/USAGE_RU.md','docs/assets/cover.svg','docs/assets/skill-map.svg']:
    if not (root / required).is_file(): errors.append({'missing_document': required})
print(json.dumps({'passed': not errors, 'skills': len(skills), 'skill_files': len(actual), 'groups': len(catalog), 'errors': errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
