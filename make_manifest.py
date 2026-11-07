"""Regenerate MANIFEST_SHA256.txt over every file in this folder (run from the deposit root)."""
import hashlib, os
root = os.path.dirname(os.path.abspath(__file__))
lines = []
for dp, dn, fn in os.walk(root):
    dn.sort()
    for f in sorted(fn):
        p = os.path.join(dp, f); rel = os.path.relpath(p, root).replace(os.sep, "/")
        if rel == "MANIFEST_SHA256.txt":
            continue
        lines.append(f"{hashlib.sha256(open(p, 'rb').read()).hexdigest()}  {rel}")
open(os.path.join(root, "MANIFEST_SHA256.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"{len(lines)} files listed")
