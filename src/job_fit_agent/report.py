from job_fit_agent.models import JobPosting, SkillComparison, StudyPlan


def to_markdown(
    job: JobPosting, comparison: SkillComparison, plan: StudyPlan | None
) -> str:
    # Artı becerileri ayır; özet ve Var/Kısmen/Yok sadece zorunluları içerir.
    # Model beceri adını değiştirirse eşleşme bulunmaz ve beceri zorunlulara düşer.
    nice = {s.lower() for s in job.nice_to_have}
    groups = {"var": [], "kısmen": [], "yok": []}
    extras = []
    for m in comparison.matches:
        if m.job_skill.lower() in nice:
            extras.append(m)
        else:
            groups[m.status].append(m)

    lines = [
        f"# {job.title} — {job.company}",
        "",
        f"**var: {len(groups['var'])} · kısmen: {len(groups['kısmen'])} · "
        f"yok: {len(groups['yok'])}**",
        "",
    ]

    titles = {"var": "Var", "kısmen": "Kısmen", "yok": "Yok"}
    for status, title in titles.items():
        lines.append(f"## {title}")
        lines.append("")
        if not groups[status]:
            lines.append("_Yok._")
        for m in groups[status]:
            matched = f" ({m.matched_with})" if m.matched_with else ""
            lines.append(f"- **{m.job_skill}**{matched} — {m.reason}")
        lines.append("")

    lines.append("## Artı beceriler")
    lines.append("")
    if not extras:
        lines.append("_Yok._")
    for m in extras:
        lines.append(f"- **{m.job_skill}** → {m.status} — {m.reason}")
    lines.append("")

    lines.append("## Çalışma planı")
    lines.append("")
    if plan is None:
        lines.append("Eksik beceri yok, plana gerek yok.")
    else:
        for i, item in enumerate(plan.items, start=1):
            lines.append(f"{i}. **[{item.priority}] {item.skill}** — {item.why}")
            lines.append(f"   - İlk adım: {item.first_step}")

    return "\n".join(lines) + "\n"
