# AI Developer — Massive Bio

**var: 10 · kısmen: 6 · yok: 9**

## Var

- **Python** (Python) — Profilde Python doğrudan listelenmiş.
- **Pydantic** (Pydantic) — Profilde Pydantic doğrudan listelenmiş.
- **FastAPI** (FastAPI) — Profilde FastAPI doğrudan listelenmiş.
- **Microservices** (Microservices) — Profilde Microservices doğrudan listelenmiş.
- **LLMs** (LLMs) — Profilde LLMs doğrudan listelenmiş.
- **Vector Databases** (Vector Databases) — Profilde Vector Databases doğrudan listelenmiş.
- **Qdrant** (Qdrant) — Profilde Qdrant doğrudan listelenmiş.
- **Semantic Search** (Hybrid Search) — Hybrid Search ile embedding ve vektör veritabanı deneyimi anlamsal aramayı kapsıyor.
- **RAG** (RAG) — Profilde RAG doğrudan listelenmiş.
- **Observability** (Observability) — Profilde Observability doğrudan listelenmiş.

## Kısmen

- **Async Programming** (Node.js) — Node.js ve FastAPI ile async yapılara temas olabilir ama profilde doğrudan async programlama maddesi yok.
- **Multi-agent Systems** (AI Agents) — AI Agents ve LangGraph temeli var ama çoklu ajan sistemi doğrudan belirtilmemiş.
- **GPT-4o** (Azure OpenAI) — Azure OpenAI ve LLM deneyimi var ama GPT-4o özel olarak belirtilmemiş.
- **GPT-5** (Azure OpenAI) — Azure OpenAI ve LLM deneyimi var ama GPT-5 özel olarak belirtilmemiş.
- **Error Handling** (Structured Output) — Hata yönetimi doğrudan listelenmemiş, yalnızca ilişkili yapılandırılmış çıktı doğrulama deneyimi var.
- **Event-driven Architecture** (Microservices) — Microservices temeli var ama olay güdümlü mimari doğrudan belirtilmemiş.

## Yok

- **OCR** — Profilde OCR ya da belge görüntü işleme ile ilgili beceri yok.
- **Clinical Abstraction** — Profilde klinik veri çıkarımı ile ilgili bir beceri yok.
- **Terminology Mapping** — Profilde terminoloji eşleme becerisi yok.
- **FHIR** — Profilde sağlık veri standartlarıyla ilgili beceri yok.
- **Azure FHIR** — Azure becerileri var ama FHIR ile ilgili bir deneyim yok.
- **HL7** — Profilde HL7 ya da sağlık entegrasyon standardı yok.
- **SNOMED CT** — Profilde tıbbi terminoloji becerisi yok.
- **RxNorm** — Profilde ilaç terminolojisi ile ilgili beceri yok.
- **LOINC** — Profilde laboratuvar kodlama standardı ile ilgili beceri yok.

## Artı beceriler

_Yok._

## Çalışma planı

1. **[yüksek] FHIR** — İlan sağlık verisinin standart biçimde temsil edilmesini ve aktarılmasını gerektirdiği için FHIR kaynak yapısını bilmek temel bir ön koşuldur.
   - İlk adım: Herkese açık HAPI FHIR test sunucusuna (hapi.fhir.org) bir Patient ve bir Observation kaynağı için GET isteği at, dönen JSON'daki alanları not et.
2. **[yüksek] Clinical Abstraction** — İlandaki asıl iş, serbest metin klinik notlardan yapılandırılmış bilgi çıkarmak olduğu için klinik soyutlama mantığını anlamak şarttır.
   - İlk adım: Uydurma 10 satırlık bir taburcu notu al, içinden tanı, ilaç ve laboratuvar değerlerini elle bir tabloya çıkar, ardından aynı işi Azure OpenAI ile yapan bir prompt yaz.
3. **[yüksek] Terminology Mapping** — Çıkarılan klinik kavramların standart kodlara eşlenmesi, verinin sistemler arasında tutarlı ve kullanılabilir olmasını sağlar.
   - İlk adım: Metinden çıkardığın 5 klinik terimi (ör. hipertansiyon, metformin) uygun kod sistemlerinde elle ara ve terim-kod eşleme tablosu oluştur.
4. **[yüksek] OCR** — Klinik belgelerin çoğu taranmış PDF veya görüntü olarak geldiği için metne dönüştürme adımı işlem hattının girişini oluşturur.
   - İlk adım: Azure AI Document Intelligence'ın Read modeliyle taranmış tek sayfalık bir örnek belgeyi işle ve çıkan metni kontrol et.
5. **[yüksek] SNOMED CT** — SNOMED CT klinik tanı ve bulguların kodlanmasında yaygın kullanılan terminoloji olduğu için ilandaki eşleme işlerinde sık karşına çıkacaktır.
   - İlk adım: Herkese açık bir SNOMED CT tarayıcısında 'type 2 diabetes mellitus' terimini ara, kavram kimliğini ve üst-alt ilişkilerini not et.
