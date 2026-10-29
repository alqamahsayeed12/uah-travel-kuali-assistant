"""Verify and unpack the complete source tree beside this file. Python 3.10+."""
from pathlib import Path
import hashlib,zipfile
root=Path(__file__).resolve().parent
archive=root/'source-v1.1.0.zip'
expected=(root/'SHA256SUMS').read_text().split()[0]
if hashlib.sha256(archive.read_bytes()).hexdigest()!=expected:raise SystemExit('Source checksum mismatch')
with zipfile.ZipFile(archive) as z:
    for info in z.infolist():
        target=(root/info.filename).resolve()
        if not target.is_relative_to(root):raise SystemExit('Unsafe archive path')
        if target.exists() and target.name!='README.md' and target.read_bytes()!=z.read(info):raise SystemExit('Local changes would be overwritten: '+info.filename)
    for info in z.infolist():
        if info.filename=='README.md':continue
        target=root/info.filename;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(info))
print('Verified source extracted. Run: python3 scripts/build.py')
