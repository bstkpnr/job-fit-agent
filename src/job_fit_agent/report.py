from job_fit_agent.models import JobPosting, SkillComparison, StudyPlan, split_matches


def to_markdown(
    job: JobPosting, comparison: SkillComparison, plan: StudyPlan | None
) -> str:
    # Özet ve Var/Kısmen/Yok sadece zorunluları içerir; artılar ayrı bölümde
    required, extras = split_matches(job, comparison)
    groups = {"var": [], "kısmen": [], "yok": []}
    for m in required:
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
