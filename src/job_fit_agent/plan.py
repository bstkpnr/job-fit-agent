from langchain_anthropic import ChatAnthropic

from job_fit_agent.models import SkillComparison, StudyPlan

ORDER = {"yüksek": 0, "orta": 1, "düşük": 2}

INSTRUCTION = """\
Bir adayın bir iş ilanı için eksik ya da kısmen sahip olduğu beceriler aşağıda.
Bunlardan bir çalışma planı hazırla. En önemli en fazla 5 madde yaz.

Kurallar:
- Önce "yok" olanlara yüksek öncelik ver. "kısmen" olanlar orta ya da düşük olsun.
- "kısmen" olanlar için ilk adım kısa olsun, çünkü adayın temeli var.
- first_step somut ve bugün yapılabilir olsun. "LangChain öğren" gibi genel ifadeler
  yerine "LangChain ile 20 satırlık bir RAG zinciri yaz" gibi bir görev yaz.
- why alanında bu becerinin bu ilan için neden önemli olduğunu tek cümleyle yaz.
- Her madde listedeki tek bir beceri için olsun; aynı beceriyi iki kez yazma.
"""


def make_plan(comparison: SkillComparison) -> StudyPlan:
    gaps = [m for m in comparison.matches if m.status in ("yok", "kısmen")]

    lines = []
    for m in gaps:
        if m.status == "kısmen" and m.matched_with:
            lines.append(f"- {m.job_skill} (kısmen: {m.matched_with} var)")
        else:
            lines.append(f"- {m.job_skill} ({m.status})")

    llm = ChatAnthropic(model="claude-sonnet-5-5")
    structured_llm = llm.with_structured_output(StudyPlan, method="json_schema")
    plan = structured_llm.invoke(f"{INSTRUCTION}\n" + "\n".join(lines))

    # Öncelik sırasına göre diz ve ilk 5'i al
    items = sorted(plan.items, key=lambda i: ORDER[i.priority])[:5]
    return StudyPlan(items=items)
