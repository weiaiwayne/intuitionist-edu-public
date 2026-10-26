#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check the explicit public-file inventory, links and obvious sensitive patterns.

This utility checks a documentation release; it is not an agent runtime, a secret
scanner with complete coverage, or a substitute for rights/privacy review.
"""
from pathlib import Path
import hashlib,json,re,sys
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1]
def check(root):
 root=Path(root).resolve();errors=[];manifest=root/'release-manifest.json'
 try:m=json.loads(manifest.read_text())
 except Exception as e:return ['Cannot read release manifest: '+str(e)]
 listed=m.get('files',{});seen=set()
 for p in root.rglob('*'):
  rel=p.relative_to(root).as_posix()
  if '.git' in p.relative_to(root).parts:continue
  if p.is_symlink():errors.append('Symlink not permitted: '+rel);continue
  if not p.is_file():continue
  seen.add(rel)
  if rel=='release-manifest.json':continue
  if rel not in listed:errors.append('Unexpected file: '+rel);continue
  raw=p.read_bytes()
  if hashlib.sha256(raw).hexdigest()!=listed[rel].get('sha256'):errors.append('Changed content; review required: '+rel)
  if len(raw)>300000:errors.append('Unexpected large file: '+rel)
  try:text=raw.decode('utf-8')
  except UnicodeDecodeError:errors.append('Non-text file not reviewed: '+rel);continue
  patterns={
   'private key':r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',
   'GitHub token':r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{35,})\b',
   'Discord mention or private channel link':r'<@!?\d{15,}>|discord(?:app)?\.com/channels/\d+',
   'private machine path':r'/root/(?:clawd|\.hermes|\.codex)/',
   'cloud access key':r'\bAKIA[A-Z0-9]{16}\b',
   'credential assignment':r'(?i)(?:api[_-]?key|access[_-]?token|password)\s*[:=]\s*["\x27][A-Za-z0-9_+/=-]{16,}["\x27]',
  }
  for kind,pat in patterns.items():
   if re.search(pat,text):errors.append(kind+': '+rel)
  if p.suffix=='.md':
   for target in re.findall(r'\]\(([^)]+)\)',text):
    target=target.split()[0].strip('<>');u=urlsplit(target)
    if u.scheme or not u.path:continue
    dest=(p.parent/unquote(u.path)).resolve()
    if not dest.is_relative_to(root) or not dest.exists():errors.append('Broken/outside link: '+rel+' -> '+target)
 for rel in listed:
  if rel not in seen:errors.append('Listed file missing: '+rel)
 if m.get('scope')!='framework-and-tech-stack-only':errors.append('Unexpected release scope')
 return errors
if __name__=='__main__':
 errors=check(ROOT)
 if errors:
  print('\n'.join(errors),file=sys.stderr);raise SystemExit(1)
 print('PASS: explicit file inventory, content hashes, local links, text-only boundary and sensitive-pattern checks')
