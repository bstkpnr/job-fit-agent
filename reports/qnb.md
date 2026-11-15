# AI Engineer / AI Agent Developer — QNB

**var: 19 · kısmen: 6 · yok: 2**

## Var

- **Python** (Python) — Profilde Python doğrudan listelenmiş.
- **LLM Agents** (AI Agents) — AI Agents ve LLMs becerileri LLM tabanlı ajanları kapsıyor.
- **Tool Calling** (Tool Calling) — Profilde Tool Calling doğrudan var.
- **Function Calling** (Tool Calling) — Function calling ile tool calling aynı mekanizmayı ifade eder.
- **RAG** (RAG) — Profilde RAG doğrudan var.
- **MCP** (MCP) — Profilde MCP doğrudan listelenmiş.
- **Tool-use Design** (Tool Calling) — Tool Calling ve Context Engineering araç kullanımı tasarımını gösteriyor.
- **API Integration** (REST APIs) — REST APIs ve SDK Integration API entegrasyonunu doğrudan gösteriyor.
- **Output Validation** (Pydantic) — Pydantic ve Structured Output çıktı doğrulamayı kapsıyor.
- **Prompt Engineering** (Prompt Engineering) — Profilde doğrudan var.
- **Context Engineering** (Context Engineering) — Profilde doğrudan var.
- **LLM APIs** (Azure OpenAI) — Azure OpenAI ve LLMs LLM API kullanımını doğrudan gösteriyor.
- **LangChain** (LangChain) — Profilde doğrudan var.
- **LangGraph** (LangGraph) — Profilde doğrudan var.
- **Vector Databases** (Vector Databases) — Profilde Vector Databases ve Qdrant var.
- **Embedding Models** (Embedding Models) — Profilde doğrudan var.
- **REST APIs** (REST APIs) — Profilde doğrudan var.
- **Microservices** (Microservices) — Profilde doğrudan var.
- **Software Engineering** (Git) — 4 yıl yazılım geliştirme deneyimi, Git ve CI/CD pratikleri var.

## Kısmen

- **Multi-agent Workflows** (AI Agents) — AI Agents ve LangGraph var ama çoklu ajan iş akışı doğrudan belirtilmemiş.
- **Agent Orchestration** (LangGraph) — LangGraph orkestrasyon için ilgili bir temel sağlıyor ancak doğrudan bir madde yok.
- **Memory** (RAG) — RAG ve vektör veritabanı ilgili ama ajan hafızası doğrudan belirtilmemiş.
- **Guardrails** (Structured Output) — Structured Output ve Pydantic ilgili ama guardrails doğrudan yok.
- **LlamaIndex** (LangChain) — LangChain benzer bir çerçeve olduğu için öğrenmesi kolay.
- **Langflow** (LangChain) — Langflow LangChain üzerine kurulu görsel bir araç, LangChain bilgisi temel sağlar.

## Yok

- **Fine-tuning** — Profilde model ince ayarı ile ilgili madde yok.
- **LoRA** — Profilde LoRA veya parametre verimli ince ayar yok.

## Artı beceriler

- **Model Serving** → kısmen — FastAPI ile servis geliştirme deneyimi var ama model serving doğrudan belirtilmemiş.
- **Self-hosted LLMs** → yok — Profilde kendi sunucuda LLM barındırma deneyimi görünmüyor, yalnızca Azure OpenAI var.
- **Open-source LLMs** → yok — Profilde açık kaynak LLM kullanımını gösteren madde yok.
- **Speech Technologies** → yok — Profilde konuşma teknolojileriyle ilgili beceri yok.
- **STT** → yok — Profilde konuşmadan metne dair beceri yok.
- **TTS** → yok — Profilde metinden konuşmaya dair beceri yok.
- **Voice-based Agents** → kısmen — AI Agents var ama sesli ajan deneyimi yok.
- **English** → var — Profilde English (B2) var.

## Çalışma planı

1. **[yüksek] Fine-tuning** — İlan, hazır modelleri kullanmanın ötesinde modeli kendi veri ve göreve göre uyarlayabilen birini aradığı için fine-tuning temel bir gereksinimdir.
   - İlk adım: Hugging Face'ten küçük bir modeli (ör. 100-500 örnekli bir sınıflandırma veri setiyle) Colab üzerinde 1 epoch fine-tune et ve eğitim öncesi/sonrası çıktıları karşılaştır.
2. **[yüksek] LoRA** — Fine-tuning'i düşük maliyetle ve sınırlı GPU ile yapabilmek için LoRA gibi parametre-verimli yöntemler pratikte neredeyse zorunludur.
   - İlk adım: Hugging Face PEFT kütüphanesiyle küçük bir modele r=8 ayarlı bir LoRA adaptörü ekle ve eğitilebilir parametre sayısını yazdır.
3. **[orta] Multi-agent Workflows** — İlandaki ajan tabanlı sistemler genellikle birden fazla ajanın görev paylaşarak çalışmasını gerektirir.
   - İlk adım: Mevcut ajan bilgini kullanarak biri araştırıp diğeri özetleyen iki ajanlı basit bir akış yaz.
4. **[orta] Agent Orchestration** — Ajanların sırasını, durumunu ve hata yönetimini koordine etmek ilandaki üretim seviyesi ajan sistemlerinin merkezindedir.
   - İlk adım: LangGraph'ta koşullu bir kenar içeren 3 düğümlü bir graf kur (ör. yönlendirici, araç çağıran, yanıtlayıcı).
5. **[orta] Guardrails** — Üretimdeki LLM çıktılarının güvenli, doğrulanmış ve beklenen formatta olması ilan için kritik bir kalite şartıdır.
   - İlk adım: Var olan structured output şemana bir Pydantic doğrulaması ve geçersiz çıktıda tek seferlik yeniden deneme ekle.
