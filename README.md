# job-fit-agent

Bir iş ilanını okuyup adayın profiliyle karşılaştıran bir yapay zekâ agent'ı. İlandaki her beceri için adayda **var**, **kısmen** ya da **yok** kararı verir, kısa bir gerekçe yazar ve eksikler için bir çalışma planı çıkarır.

LangGraph, Claude (Anthropic) ve Pydantic ile geliştirildi.

**Demo:** [bstkpnr.github.io/job-fit-agent](https://bstkpnr.github.io/job-fit-agent/): 6 gerçek ilanın (şirket adları gizlenmiş) raporları. Demo `demo/` klasöründe (Vite + React); veri `export_demo.py` ile üretilir, `demo/` değişince GitHub Actions otomatik deploy eder.

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
| `eval_compare.py` | Karşılaştırma adımını golden set ile ölçer (doğruluk ve tutarlılık) |
| `server.py` | Agent'ı Claude Desktop'a tool olarak sunan MCP sunucusu |
| `collect_skills.py` | Raporlardaki ilan becerilerini sayar (ilanlar arası en sık beceriler) |
| `export_demo.py` | Raporları şirket adlarını maskeleyerek `demo/src/data/` klasörüne aktarır |
| `score.py` | 0-100 uyum skoru (kodla hesaplanır, modele sorulmaz) ve düşük güven işareti |
| `rank.py` | Raporlardaki ilanları uyum skoruna göre sıralar |
| `api.py` | `POST /analyze` endpoint'i (FastAPI, API anahtarı korumalı) |
| `n8n/job-fit-email.json` | E-postayla gelen ilanı analiz edip cevap gönderen n8n workflow'u |

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
uv run --env-file .env python src/job_fit_agent/graph.py jobs/example.txt
```

İlan metni `jobs/` klasöründeki bir `.txt` dosyasından okunur; rapor aynı adla `reports/` klasörüne Markdown ve JSON olarak yazılır (`jobs/example.txt` → `reports/example.md`, `reports/example.json`). Yeni bir ilanı denemek için metnini `jobs/` altına kaydetmen yeterli.

`jobs/` ve `reports/` yerel çalışma verisidir, repoya girmez (`.gitignore`). Repoda sadece kurgusal örnek ilan `jobs/example.txt` bulunur.

İlk çalıştırmada embedding modeli (`paraphrase-multilingual-MiniLM-L12-v2`) indirilir.

Kendi profilinle denemek için `profile.py` içindeki beceri listesini ve deneyim yılını değiştir.

### Claude Desktop'tan kullanmak (MCP)

Agent, `analyze_job_posting` adlı bir MCP tool'u olarak da çalışır. Claude Desktop'ta bir ilanı yapıştırıp "Bu ilana ne kadar uygunum?" diye sorduğunda Claude bu tool'u çağırır.

`~/Library/Application Support/Claude/claude_desktop_config.json` dosyasına ekle (`which uv` çıktısını ve kendi proje yolunu yaz):

```json
{
  "mcpServers": {
    "job-fit-agent": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "--directory", "/path/to/job-fit-agent",
        "run",
        "python", "src/job_fit_agent/server.py"
      ]
    }
  }
}
```

Sunucu `.env` dosyasını kendisi okur. Claude Desktop'ı Cmd+Q ile kapatıp yeniden aç.

Test için MCP Inspector:

```bash
uv run mcp dev src/job_fit_agent/server.py
```

### HTTP API (`/analyze`)

`.env` dosyasına bir API anahtarı ekle (değeri üretmek için `python -c "import secrets; print(secrets.token_urlsafe(32))"`):

```
API_KEY=...
```

Sunucuyu başlat:

```bash
uv run --env-file .env uvicorn job_fit_agent.api:app
```

`POST /analyze` gövdesinde `{"job_text": "..."}` alır (200–20.000 karakter), `X-API-Key` header'ı ister. Cevapta `job`, `comparison`, `plan`, `score` ve e-postaya konmaya hazır `markdown` alanları döner. Doküman ve deneme ekranı: http://127.0.0.1:8000/docs

Endpoint düz `def` ile yazıldı, `async def` değil: analiz ~25 sn bloklayan bir çağrı; düz `def` ayrı bir thread'de çalıştığı için sunucu bu sırada başka isteklere cevap vermeye devam eder.

### E-postayla kullanmak (n8n)

```
"ilan" konulu e-posta → n8n (IMAP) → POST /analyze → Markdown → HTML → cevap e-postası (SMTP)
```

Kendine konusu "ilan" olan bir e-posta atıp gövdeye ilan metnini yapıştırırsın; birkaç dakika içinde "Uyum %84 — AI Engineer" gibi bir konuyla rapor gelir.

Kurulum:

1. API sunucusunu başlat (yukarıdaki bölüm) ve n8n'i çalıştır: `npx n8n` → http://localhost:5678
2. Gmail'de [uygulama şifresi](https://myaccount.google.com/apppasswords) oluştur (2 adımlı doğrulama açık olmalı). Normal Gmail şifren değil, bu şifre kullanılır.
3. n8n'de **Import from File** ile `n8n/job-fit-email.json` dosyasını aç.
4. `SENIN_ADRESIN@gmail.com` yazan 3 yeri kendi adresinle değiştir: Gmail node'undaki `FROM` filtresi, cevap e-postasının From ve To alanları. `FROM` filtresi önemli: o olmazsa sana "ilan" konulu e-posta gönderen herkes ücretli bir analiz başlatabilir.
5. Credential'ları oluştur:

| Node | Tür | Ayarlar |
|---|---|---|
| Gmail | IMAP | `imap.gmail.com`, port `993`, SSL açık, kullanıcı adı Gmail adresin, şifre uygulama şifresi |
| Cevap e-postası | SMTP | `smtp.gmail.com`, port `465`, SSL açık, aynı kullanıcı ve şifre |
| POST /analyze | Header Auth | Name `X-API-Key`, Value `.env`'deki `API_KEY` |

6. Kendine bir "ilan" e-postası at (açmadan bırak, sadece okunmamışlar alınır), **Execute workflow** ile dene, çalışınca workflow'u **Active** yap.

Notlar:

- URL `http://127.0.0.1:8000`, `localhost` değil: Node.js (n8n) `localhost`'u önce IPv6 (`::1`) olarak dener, uvicorn ise sadece IPv4'te dinler.
- Şifreler ve API anahtarı workflow dosyasında değil, n8n'in kendi veritabanında (`~/.n8n`) şifreli tutulur.
- Akış iki sunucunun da (API ve n8n) açık olmasını gerektirir.

### İzleme (Langfuse)

`.env` dosyasına `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY` ve `LANGFUSE_BASE_URL` eklenirse her çalıştırma Langfuse'a trace olarak gönderilir: her node'un süresi, token kullanımı ve maliyeti görünür.

### Değerlendirme (eval)

```bash
uv run --env-file .env python src/job_fit_agent/eval_compare.py
```

Karşılaştırma adımı, elle etiketlenmiş 12 beceri üzerinde 3 kez çalıştırılır. Doğruluk (golden set ile uyuşan cevaplar) ve tutarlılık (3 çalıştırmada aynı cevabı alan beceriler) ayrı ayrı raporlanır.

### Sonuçlar (eval)

Sonuçlar: doğruluk %33 → %75 → **%94**, tutarlılık **%83**. İlk turdaki hataların çoğu modelden değil, profildeki eksik veriden geliyordu. Süreç [Gün 10 yazısında](https://medium.com/@bstkpnr/ai-engineer-oluyoruz-agent%C4%B1-%C3%B6l%C3%A7mek-ce413f564a16?postPublishedType=initial) anlatılıyor.

## Yol haritası

- [x] İlandan yapılandırılmış bilgi çıkarma
- [x] İlk LangGraph akışı
- [x] Embedding + LLM ile beceri karşılaştırma
- [x] Karşılaştırmayı LangGraph'a node olarak eklemek
- [x] Eksik becerilere göre çalışma planı çıkaran node (koşullu edge)
- [x] İlanı dosyadan okuma ve Markdown rapor
- [x] Golden set ile eval
- [x] Langfuse ile izleme
- [x] MCP sunucusu (Claude Desktop entegrasyonu)
- [x] Artı becerileri ayrı değerlendirme
- [x] Uyum skoru ve ilan sıralama
- [x] Anonim demo sayfası (`demo/`)
- [x] HTTP API (`/analyze`)
- [x] E-postayla analiz (n8n)
