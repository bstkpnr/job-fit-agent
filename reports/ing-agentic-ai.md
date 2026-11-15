# Agentic AI / Data Science — ING

**var: 5 · kısmen: 10 · yok: 3**

## Var

- **Agentic AI** (AI Agents) — Profilde AI Agents, LangGraph ve Tool Calling gibi ajan tabanlı yapay zeka becerileri doğrudan var.
- **LLM** (LLMs) — Profilde LLMs becerisi doğrudan listelenmiş.
- **LangGraph** (LangGraph) — Profilde LangGraph doğrudan var.
- **Python** (Python) — Profilde Python doğrudan var.
- **Machine Learning** (Machine Learning) — Profilde Machine Learning doğrudan var.

## Kısmen

- **Multi-agent Systems** (AI Agents) — AI Agents ve LangGraph var ancak çoklu ajan sistemi deneyimini doğrudan gösteren bir madde yok.
- **CrewAI** (AI Agents) — Ajan çerçevesi deneyimi (LangGraph, LangChain) var ama CrewAI bilgisi yok, öğrenmesi kolay.
- **AutoGen** (AI Agents) — Ajan çerçevesi deneyimi var ama AutoGen'e özel bir beceri görünmüyor.
- **Google ADK** (AI Agents) — Ajan geliştirme temeli var ancak Google ADK bilgisi profilde yok.
- **OpenAI Agents SDK** (AI Agents) — Azure OpenAI ve ajan deneyimi var ama OpenAI Agents SDK doğrudan belirtilmemiş.
- **Neural Networks** (Machine Learning) — Makine öğrenmesi ve LLM bilgisi var ama sinir ağlarını doğrudan gösteren bir madde yok.
- **Data Science** (Predictive Modeling) — Predictive Modeling, Machine Learning ve SQL var ama genel veri bilimi deneyimi doğrudan belirtilmemiş.
- **Information Extraction** (Structured Output) — Structured Output, RAG ve Chunking ilgili ancak bilgi çıkarımı doğrudan listelenmemiş.
- **Document Understanding** (Chunking) — Chunking ve RAG ilgili ama doküman anlama doğrudan belirtilmemiş.
- **KYC Automation** (KYC) — KYC ve yapay zeka ajan deneyimi var ama KYC otomasyonu doğrudan belirtilmemiş.

## Yok

- **Entity Resolution** — Profilde varlık eşleştirme ile ilgili bir beceri yok.
- **Graph Analytics** — Profilde graf analitiği ile ilgili bir beceri yok.
- **Network Analysis** — Profilde ağ analizi ile ilgili bir beceri yok.

## Artı beceriler

- **Model Governance** → kısmen — Evals ve Observability ilgili ama model yönetişimi doğrudan yok.
- **Wholesale Banking** → kısmen — Ödeme sistemleri ve KYC bankacılıkla ilgili ama toptan bankacılık deneyimi belirtilmemiş.
- **KYC** → var — Profilde KYC doğrudan var.
- **AML** → kısmen — KYC, AML ile komşu bir alan ama AML doğrudan profilde yok.
- **Financial Crime** → kısmen — KYC finansal suç alanıyla ilişkili ama doğrudan finansal suç deneyimi yok.
- **Regulated Industries** → kısmen — KYC ve ödeme sistemleri düzenlemeye tabi alanlarla ilgili ama doğrudan belirtilmemiş.

## Çalışma planı

1. **[yüksek] Entity Resolution** — KYC ve finansal suç odaklı bu ilanda farklı kaynaklardaki kayıtların aynı kişi ya da kuruma ait olup olmadığını eşleştirmek temel bir iştir.
   - İlk adım: Python'da recordlinkage veya rapidfuzz ile 20 satırlık sahte müşteri listesinde isim ve adres benzerliğine göre yinelenen kayıtları eşleştiren bir script yaz.
2. **[yüksek] Graph Analytics** — İlandaki kuruluşlar arası ilişkileri ve şüpheli işlem zincirlerini ortaya çıkarmak graf tabanlı analiz gerektirir.
   - İlk adım: Neo4j Aura ücretsiz hesabı aç ve 10 müşteri ile 15 işlemden oluşan küçük bir grafı Cypher ile yükleyip ortak hesabı paylaşan müşterileri sorgula.
3. **[yüksek] Network Analysis** — Hesaplar ve işlemler arasındaki ağ yapısını ölçerek kümeleri ve merkezi düğümleri bulmak bu ilandaki risk tespiti çalışmalarının parçasıdır.
   - İlk adım: Python'da NetworkX ile 30 kenarlı örnek bir işlem ağı oluştur ve degree ile betweenness centrality değerlerini hesaplayıp en yüksek 3 düğümü yazdır.
4. **[orta] Multi-agent Systems** — İlan, birden fazla ajanın görev paylaşarak çalıştığı sistemler kurulmasını beklediği için tek ajan deneyimi yeterli olmaz.
   - İlk adım: Mevcut ajan bilgini kullanarak biri belge okuyan, diğeri okunan bilgiyi doğrulayan iki ajanın mesajlaştığı basit bir akışı çiz ve kodla.
5. **[orta] Information Extraction** — KYC belgelerinden isim, tarih ve adres gibi alanları güvenilir biçimde çıkarmak ilandaki otomasyonun temelidir.
   - İlk adım: Elindeki structured output bilginle bir sahte kimlik metninden ad, doğum tarihi ve adresi Pydantic şemasına çıkaran 15 satırlık bir LLM çağrısı yaz.
