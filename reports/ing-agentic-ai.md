# Agentic AI / Data Science — ING

**var: 5 · kısmen: 10 · yok: 4**

## Var

- **Agentic AI** (AI Agents) — Profilde AI Agents ve LangGraph gibi ajan tabanlı beceriler doğrudan var.
- **LLM** (LLMs) — Profilde LLMs becerisi doğrudan yer alıyor.
- **LangGraph** (LangGraph) — Profilde LangGraph doğrudan var.
- **Python** (Python) — Profilde Python doğrudan var.
- **Machine Learning** (Machine Learning) — Profilde Machine Learning doğrudan var.

## Kısmen

- **Multi-agent systems** (AI Agents) — AI Agents ve LangGraph temeli var ama çoklu ajan sistemi deneyimi açıkça belirtilmemiş.
- **CrewAI** (LangChain) — Benzer ajan çerçeveleri biliniyor ama CrewAI profilde yok.
- **AutoGen** (AI Agents) — Ajan geliştirme temeli var ama AutoGen çerçevesi profilde yok.
- **Google ADK** (AI Agents) — Ajan geliştirme deneyimi var ama Google ADK profilde yok.
- **OpenAI Agents SDK** (Azure OpenAI) — Azure OpenAI ve ajan deneyimi var ama OpenAI Agents SDK doğrudan yok.
- **Neural Networks** (Machine Learning) — ML temeli var ama sinir ağları açıkça belirtilmemiş.
- **Data Science** (Predictive Modeling) — Machine Learning ve Predictive Modeling ilgili ama veri bilimi doğrudan belirtilmemiş.
- **Document understanding** (Structured Output) — LLM ile yapılandırılmış çıktı deneyimi ilgili ama doküman anlama doğrudan yok.
- **Information extraction** (Structured Output) — Structured Output ve RAG ilgili ama bilgi çıkarımı doğrudan belirtilmemiş.
- **Communication** (English (B2)) — İngilizce B2 var ama iletişim becerisi doğrudan belirtilmemiş.

## Yok

- **Entity resolution** — Profilde varlık eşleştirme ile ilgili bir beceri yok.
- **Graph analytics** — Profilde graf analitiği ile ilgili bir beceri yok.
- **Network analysis** — Profilde ağ analizi ile ilgili bir beceri yok.
- **Stakeholder engagement** — Profilde paydaş yönetimi ile ilgili bir madde yok.

## Artı beceriler

- **Model governance** → yok — Profilde model yönetişimi ile ilgili bir beceri yok.
- **Wholesale Banking** → kısmen — Ödeme sistemleri ve KYC bankacılıkla ilgili ama toptan bankacılık doğrudan yok.
- **KYC** → var — Profilde KYC doğrudan var.
- **AML** → kısmen — KYC, AML ile ilişkili ama AML doğrudan profilde yok.
- **Financial crime** → kısmen — KYC finansal suç önleme ile ilgili ama doğrudan finansal suç deneyimi yok.
- **Regulated industries** → kısmen — KYC ve ödeme sistemleri düzenlenen sektörlerle ilgili ama açık bir ifade yok.

## Çalışma planı

1. **[yüksek] Entity resolution** — İlan, farklı kaynaklardaki kayıtların aynı kişi ya da kurumla eşleştirilmesini gerektiren veri işleri için bu beceriyi merkeze koyuyor.
   - İlk adım: Python'da recordlinkage veya rapidfuzz ile 50 satırlık sahte bir müşteri listesinde isim ve adres benzerliğine göre yinelenen kayıtları eşleştiren bir script yaz.
2. **[yüksek] Graph analytics** — İlişkisel veriden gizli bağlantıları ve riskli kümeleri bulmak ilanın temel analitik beklentilerinden biri.
   - İlk adım: Neo4j Aura ücretsiz hesabı aç, 10 düğümlük bir müşteri-hesap grafiği oluştur ve ortak hesabı olan müşterileri bulan bir Cypher sorgusu yaz.
3. **[yüksek] Network analysis** — İlan, varlıklar arasındaki bağlantı yapısını ölçüp yorumlayabilen adayları arıyor.
   - İlk adım: NetworkX ile 30 kenarlı küçük bir işlem ağı kur, degree ve betweenness centrality değerlerini hesaplayıp en merkezi 3 düğümü yorumla.
4. **[yüksek] Stakeholder engagement** — Teknik çözümlerin iş birimleri ve yöneticilerle birlikte şekillendirilmesi bu rolün başarısı için gerekli.
   - İlk adım: Son bir projeni seç ve paydaşlarını, her birinin beklentisini ve onlara vereceğin güncelleme sıklığını gösteren yarım sayfalık bir paydaş haritası çıkar.
5. **[orta] Multi-agent systems** — İlan, birden fazla ajanın birlikte çalıştığı sistemler kurabilen adayları hedefliyor.
   - İlk adım: Mevcut ajan bilgini kullanarak bir araştırmacı ve bir özetleyici ajanı birbirine mesaj geçirecek şekilde bağlayan 30 satırlık bir prototip yaz.
