# AI Developer — Massive Bio

**var: 11 · kısmen: 5 · yok: 10**

## Var

- **Python** (Python) — Profilde Python doğrudan listelenmiş.
- **Pydantic** (Pydantic) — Profilde Pydantic doğrudan var.
- **FastAPI** (FastAPI) — Profilde FastAPI doğrudan var.
- **AI agents** (AI Agents) — Profilde AI Agents doğrudan var.
- **Python microservices** (Microservices) — Microservices ve Python ile FastAPI birlikte profilde mevcut.
- **LLMs** (LLMs) — Profilde LLMs doğrudan var.
- **Vector databases** (Vector Databases) — Profilde Vector Databases doğrudan var.
- **Qdrant** (Qdrant) — Profilde Qdrant doğrudan var.
- **RAG** (RAG) — Profilde RAG doğrudan var.
- **Semantic search** (Hybrid Search) — Hybrid Search, Embedding Models ve Vector Databases semantik aramayı kapsıyor.
- **English** (English (B2)) — Profilde English (B2) var.

## Kısmen

- **async/await** (Node.js) — Node.js ve JavaScript/Python deneyimi async kullanımını çağrıştırıyor ama profilde doğrudan async/await maddesi yok.
- **Multi-agent pipelines** (AI Agents) — AI Agents ve LangGraph var ama multi-agent pipeline açıkça belirtilmemiş.
- **GPT-4o** (Azure OpenAI) — Azure OpenAI ve LLM deneyimi var ama GPT-4o özel olarak belirtilmemiş.
- **GPT-5** (Azure OpenAI) — Azure OpenAI ve LLM deneyimi var ama GPT-5 özel olarak belirtilmemiş.
- **Error handling** (Structured Output) — Structured Output ve Pydantic doğrulama ilişkili ama hata yönetimi doğrudan belirtilmemiş.

## Yok

- **OCR** — Profilde OCR ya da görüntüden metin çıkarma ile ilgili beceri yok.
- **Clinical abstraction** — Profilde klinik veri çıkarımı deneyimi gösteren bir madde yok.
- **Terminology mapping** — Profilde terminoloji eşleme ile ilgili doğrudan beceri yok.
- **FHIR** — Profilde sağlık veri standardı FHIR'a dair beceri yok.
- **Azure FHIR** — Azure OpenAI var ama Azure FHIR servisi ve FHIR deneyimi yok.
- **HL7** — Profilde HL7 ile ilgili beceri yok.
- **SNOMED CT** — Profilde tıbbi terminoloji standardı SNOMED CT'ye dair beceri yok.
- **RxNorm** — Profilde RxNorm ile ilgili beceri yok.
- **LOINC** — Profilde LOINC ile ilgili beceri yok.
- **Observability** — Profilde izleme, loglama veya observability becerisi yok.

## Artı beceriler

_Yok._

## Çalışma planı

1. **[yüksek] FHIR** — İlan, klinik verinin FHIR standardında okunup üretilmesini bekliyor ve diğer sağlık entegrasyonlarının temeli bu standart.
   - İlk adım: Herkese açık HAPI FHIR test sunucusuna (hapi.fhir.org) bir Patient kaynağı POST et, ardından GET ile geri oku ve JSON yapısını incele.
2. **[yüksek] Clinical abstraction** — İlandaki temel iş, serbest metin klinik notlardan yapılandırılmış bilgi çıkarmak.
   - İlk adım: Uydurma 1 paragraflık bir taburcu notu yaz ve bir LLM ile tanı, ilaç ve doz alanlarını JSON olarak çıkaran bir prompt çalıştır.
3. **[yüksek] OCR** — Taranmış klinik belgelerden metin çıkarmak, bu ilandaki veri hattının ilk adımı.
   - İlk adım: Azure AI Document Intelligence ile örnek bir taranmış laboratuvar raporu PDF'ini oku ve çıkan metni dosyaya kaydet.
4. **[yüksek] Terminology mapping** — Çıkarılan klinik ifadelerin standart kodlara eşlenmesi ilanın veri kalitesi beklentisinin merkezinde.
   - İlk adım: 'tip 2 diyabet', 'hipertansiyon' ve 'metformin' gibi 10 klinik ifadeyi elle ilgili standart kodlara eşleyen küçük bir tablo hazırla.
5. **[yüksek] Azure FHIR** — İlan, FHIR verisinin Azure üzerinde yönetilmesini bekliyor.
   - İlk adım: Azure portalda Azure Health Data Services altında bir FHIR servisi oluştur ve ona bir Patient kaynağı yükle.
