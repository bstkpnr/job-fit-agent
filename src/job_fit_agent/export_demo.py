"""reports/*.json → demo/src/data/ilan-N.json (şirket adları maskelenmiş).

Kaynak raporlar yerelde kalır; demoya sadece anonim kopya çıkar.
Çalıştırma: uv run python src/job_fit_agent/export_demo.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "reports"
OUT = ROOT / "demo" / "src" / "data"

# Rapor dosyasının adı (uzantısız) → demoda görünecek etiket
LABELS = {
    "qnb": "Bir banka",
    "bim-ai-agent-developer": "Bir perakende şirketi",
    "ing-agentic-ai": "Uluslararası bir banka",
    "koc-ai-engineer": "Bir üniversite",
    "massivebio-ai-developer": "Bir sağlık teknolojisi şirketi",
    "padran-ml-engineer": "Bir BT danışmanlık şirketi",
}

# Gerçek ilan olmayan raporlar: demoya ve sıralamaya girmez.
# example.txt'yi profile göre kendimiz yazdık, %100 çıkması doğal ve yanıltıcı.
EXCLUDE = {"example"}

# Metinlerde aranacak ek adlar. job.company zaten otomatik aranıyor;
# buraya kısaltmaları ve farklı yazımları ekle.
EXTRA_NAMES = ["QNB", "BİM", "BIM", "ING", "Koç", "Koc", "Massive Bio", "massivebio", "Padran"]


def find_leaks(data: dict, names: list[str]) -> list[str]:
    """Şirket adlarının geçtiği metinleri döndürür (tam kelime, büyük/küçük harf duyarsız)."""
    texts = [data["job"]["title"], *data["job"]["required_skills"], *data["job"]["nice_to_have"]]
    for m in data["comparison"]["matches"]:
        texts += [m["job_skill"], m["reason"]]
    for item in (data["plan"] or {}).get("items", []):
        texts += [item["skill"], item["why"], item["first_step"]]

    leaks = []
    for name in names:
        # \b: "ING" adı "testing" içinde eşleşmesin
        pattern = re.compile(rf"\b{re.escape(name)}\b", re.IGNORECASE)
        leaks += [f"'{name}' → {t}" for t in texts if pattern.search(t)]
    return leaks


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    # Eski dosyaları temizle: silinen ya da eskiden ham kopyalanan raporlar kalmasın
    for old in OUT.glob("*.json"):
        old.unlink()

    files = sorted(REPORTS.glob("*.json"))
    companies = [json.loads(f.read_text(encoding="utf-8"))["job"]["company"] for f in files]
    # Boş ad (örn. şirketsiz example.txt) her metinle eşleşir; aramaya alma
    names = sorted({c.strip() for c in companies + EXTRA_NAMES if c.strip()}, key=len, reverse=True)

    n = 0
    warnings = 0
    for path in files:
        if path.stem in EXCLUDE:
            continue
        label = LABELS.get(path.stem)
        if label is None:
            # Etiketsiz rapor dışarı çıkmaz
            print(f"ATLANDI: {path.name} için LABELS'ta etiket yok")
            continue

        data = json.loads(path.read_text(encoding="utf-8"))
        data["job"]["company"] = label

        leaks = find_leaks(data, names)
        for leak in leaks:
            print(f"UYARI {path.name}: {leak}")
        warnings += len(leaks)

        n += 1
        out = OUT / f"ilan-{n}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{path.name} → {out.relative_to(ROOT)} ({label})")

    print(f"\n{n} rapor yazıldı, {warnings} uyarı.")


if __name__ == "__main__":
    main()
