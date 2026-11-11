# job-fit-agent

Bir iş ilanını okuyup adayın profiliyle karşılaştıran bir yapay zekâ agent'ı. İlandaki her beceri için adayda **var**, **kısmen** ya da **yok** kararı verir, kısa bir gerekçe yazar ve eksikler için bir çalışma planı çıkarır.

LangGraph, Claude (Anthropic) ve Pydantic ile geliştirildi.

## Nasıl çalışır?

Akış bir LangGraph grafiği olarak çalışır:

```
START → extract_job → compare_profile ─┬─ eksik var → make_plan → END
                                       └─ eksik yok → END
```

1. **extract_job** (`extract.py`): Claude ilanı okur → `JobPosting` (başlık, şirket, beceriler, deneyim yılı)
2. **compare_profile** (`compare.py`): Embedding ile her ilan becerisi için profildeki en yakın 3 beceri bulunur, Claude bunları değerlendirir → var / kısmen / yok + gerekçe
3. **make_plan** (`plan.py`): Eksik ya da kısmen olan beceriler için öncelikli, somut ilk adımlı bir çalışma planı (en fazla 5 madde)

Sonuç `reports/` klasörüne Markdown rapor olarak yazılır.

**Neden iki aşamalı eşleştirme?** Sadece embedding kullanınca kelimesi benzeyen ama anlamı farklı beceriler yüksek skor alıyor: örneğin `LoRA → RAG` (0.71) ya da `Context Engineering → Context API` (0.86). Embedding hızlı bir ön eleme yapıyor, son kararı LLM veriyor. LLM'e "benzer görünüyor diye eşleştirme, emin değilsen iyimser olma" kuralı veriliyor.

Örnek çıktı:

```
Function calling     → var     (Tool Calling)   Function calling, tool calling ile aynı mekanizmadır.
LangChain            → kısmen  (LangGraph)      LangGraph bilgisi LangChain öğrenmeyi kolaylaştırır.
LoRA                 → yok                      Adaylar LoRA ile ilgili değil.
```

## Dosyalar

| Dosya | Ne yapar |
|---|---|
| `models.py` | Pydantic modelleri: `JobPosting`, `CandidateProfile`, `SkillMatch`, `SkillComparison`, `StudyItem`, `StudyPlan` |
| `extract.py` | İlan metninden yapılandırılmış bilgi çıkarır (`with_structured_output`) |
| `graph.py` | LangGraph akışı ve komut satırı girişi |
| `plan.py` | Eksik becerilerden çalışma planı çıkarır |
| `report.py` | Sonucu Markdown rapora çevirir |
| `profile.py` | Aday profili |
| `match.py` | `fastembed` ile becerileri anlamsal olarak eşleştirir |
| `compare.py` | Embedding adaylarını LLM ile değerlendirir |

## Kurulum

[uv](https://docs.astral.sh/uv/) gerekli.

```bash
git clone https://github.com/bstkpnr/job-fit-agent.git
cd job-fit-agent
uv sync
```

Proje kök klasöründe bir `.env` dosyası oluşturup Anthropic API anahtarını ekle:

```
ANTHROPIC_API_KEY=...
```

## Çalıştırma

Komutları proje kök klasöründen çalıştır:

```bash
uv run --env-file .env python src/job_fit_agent/graph.py jobs/qnb.txt
```

İlan metni `jobs/` klasöründeki bir `.txt` dosyasından okunur; rapor aynı adla `reports/` klasörüne yazılır (`jobs/qnb.txt` → `reports/qnb.md`). Yeni bir ilanı denemek için metnini `jobs/` altına kaydetmen yeterli. Örnek çıktı: [reports/qnb.md](reports/qnb.md)

İlk çalıştırmada embedding modeli (`paraphrase-multilingual-MiniLM-L12-v2`) indirilir.

Kendi profilinle denemek için `profile.py` içindeki beceri listesini ve deneyim yılını değiştir.

## Yol haritası

- [x] İlandan yapılandırılmış bilgi çıkarma
- [x] İlk LangGraph akışı
- [x] Embedding + LLM ile beceri karşılaştırma
- [x] Karşılaştırmayı LangGraph'a node olarak eklemek
- [x] Eksik becerilere göre çalışma planı çıkaran node (koşullu edge)
- [x] İlanı dosyadan okuma ve Markdown rapor
