"""Check repository skill names, descriptions and distilled-note citations."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skills = sorted((root / ".agents/skills").glob("*/SKILL.md"))
if not skills:
    raise SystemExit("No skills found")
for skill in skills:
    header, body = skill.read_text(encoding="utf-8").split("\n---\n", 1)
    if not header.startswith("---\n") or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.parent.name):
        raise SystemExit(f"Invalid skill frontmatter or directory: {skill}")
    if f"name: {skill.parent.name}" not in header.splitlines() or not re.search(r"^description: \S.+$", header, re.M):
        raise SystemExit(f"Missing skill name or description: {skill}")
    refs = re.findall(r"\[\[([a-z0-9-]+)\]\]", body)
    if not any((root / "brain/resources" / (ref + ".md")).is_file() for ref in refs):
        raise SystemExit(f"Missing distilled note citation: {skill}")
    print(f"Validated {skill.parent.name}")
