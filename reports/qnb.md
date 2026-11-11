# AI Engineer / AI Agent Developer — QNB

**var: 13 · kısmen: 11 · yok: 4**

## Var

- **Python** (Python) — Profilde Python doğrudan mevcut.
- **LLM APIs** (LLMs) — LLM'ler ve Azure OpenAI gibi API deneyimi profilde görünüyor, LLMs becerisi bunu kapsıyor.
- **LLM-based Agents** (AI Agents) — AI Agents becerisi LLM tabanlı ajanları kapsıyor.
- **Tool Calling** (Tool Calling) — Profilde Tool Calling doğrudan mevcut.
- **Function Calling** (Tool Calling) — Function calling ile tool calling aynı mekanizmayı ifade ediyor.
- **RAG** (RAG) — Profilde RAG doğrudan mevcut.
- **Output Validation** (Structured Output) — Structured Output çıktı doğrulamayı (şema, Pydantic) kapsıyor.
- **Prompt Engineering** (Prompt Engineering) — Profilde doğrudan mevcut.
- **LangGraph** (LangGraph) — Profilde LangGraph doğrudan mevcut.
- **Vector Databases** (Vector Databases) — Profilde doğrudan mevcut.
- **Embedding Models** (Embedding Models) — Profilde doğrudan mevcut.
- **REST APIs** (REST APIs) — Profilde doğrudan mevcut.
- **API Integration** (SDK Integration) — SDK ve REST API entegrasyonu API entegrasyonunu kapsıyor.

## Kısmen

- **Multi-agent Workflows** (AI Agents) — AI Agents ilgili ama çoklu ajan iş akışı açıkça belirtilmemiş.
- **Agent Orchestration** (AI Agents) — Ajan deneyimi var ancak orkestrasyon açıkça belirtilmemiş.
- **Memory** (RAG) — RAG bellek yaklaşımlarıyla ilişkili ama ajan belleği ile aynı değil.
- **Tool-use Design** (Tool Calling) — Tool Calling bilgisi var ama araç tasarımı ayrı bir beceri.
- **Multi-agent Architectures** (AI Agents) — AI Agents ilgili ama çoklu ajan mimarisi belirtilmemiş.
- **Guardrails** (Prompt Engineering) — Prompt tasarımı güvenlik sınırlarına kısmen katkı sağlar ama guardrails değildir.
- **Context Engineering** (Prompt Engineering) — Prompt Engineering yakın ama bağlam mühendisliği daha geniş.
- **LangChain** (LangGraph) — LangGraph bilgisi LangChain öğrenmeyi kolaylaştırır.
- **LlamaIndex** (RAG) — RAG deneyimi LlamaIndex'e yakın ama araç bilgisi doğrulanmıyor.
- **Langflow** (LangGraph) — LangGraph ilgili ekosistemde, Langflow'u öğrenmek kolay olur.
- **Software Engineering** (SDK Integration) — SDK Integration yazılım geliştirme pratiğiyle ilgili ama genel yazılım mühendisliğini kapsamaz.

## Yok

- **Model Context Protocol** — Adaylar arasında MCP ile ilgili gerçek bir beceri yok; Context API React'e ait ve farklı.
- **Fine-tuning** — Adaylar arasında model ince ayarı ile ilgili beceri yok.
- **LoRA** — Adaylar LoRA ile ilgili değil.
- **Microservices** — Adaylar arasında mikroservis mimarisiyle ilgili açık bir beceri yok.

## Çalışma planı

1. **[yüksek] Model Context Protocol** — MCP, ajanların araçlara ve veri kaynaklarına standart biçimde bağlanmasını sağladığı için ilanın modern ajan altyapısı beklentisiyle doğrudan ilgilidir.
   - İlk adım: Resmi MCP Python SDK'sını kur ve tek bir 'toplama' aracı sunan 20 satırlık bir MCP sunucusu yazıp bir istemciyle çağır.
2. **[yüksek] Fine-tuning** — İlan, modelleri belirli görevlere uyarlayabilen adayları tercih ettiği için fine-tuning temelini bilmek gerekir.
   - İlk adım: Hugging Face'te küçük bir veri setiyle (100 örnek) küçük bir modeli Colab'da ince ayarlayan hazır bir not defterini çalıştır.
3. **[yüksek] LoRA** — LoRA, büyük modelleri düşük maliyetle uyarlamanın yaygın yolu olduğu için ilandaki fine-tuning beklentisinin pratik parçasıdır.
   - İlk adım: PEFT kütüphanesiyle küçük bir modele LoRA adaptörü ekleyip eğitilebilir parametre sayısını yazdır.
4. **[yüksek] Microservices** — Ajan sistemleri genelde ayrı servisler olarak dağıtıldığı için mikroservis mimarisi bilgisi ilanın yazılım altyapısı beklentisini karşılar.
   - İlk adım: FastAPI ile iki ayrı küçük servis yaz ve birinin diğerini HTTP üzerinden çağırmasını sağla, ikisini de Docker Compose ile ayağa kaldır.
5. **[orta] Multi-agent Workflows** — İlan, birden fazla ajanın birlikte çalıştığı iş akışları kurabilen birini aradığı için mevcut AI Agents deneyiminin bu yönde genişletilmesi gerekiyor.
   - İlk adım: Bir araştırmacı ve bir yazar ajanın birbirine çıktı devrettiği 2 ajanlı basit bir akışı bugün kodla.
