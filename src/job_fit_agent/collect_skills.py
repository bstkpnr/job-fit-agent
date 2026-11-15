import json
from collections import Counter
from pathlib import Path

# reports/*.json dosyalarındaki ilan becerilerini toplayıp sayar
counts: Counter[str] = Counter()
files = sorted(Path("reports").glob("*.json"))
for path in files:
    job = json.loads(path.read_text(encoding="utf-8"))["job"]
    skills = job["required_skills"] + job["nice_to_have"]
    # Aynı ilanda iki kez geçen beceri bir kez sayılsın
    counts.update({s.lower() for s in skills})

print(f"{len(files)} ilan, {len(counts)} farklı beceri\n")
for skill, n in counts.most_common():
    print(f"{n:<3}{skill}")
