from typing import Literal

from pydantic import BaseModel, Field


class JobPosting(BaseModel):
    title: str
    company: str
    required_skills: list[str] = Field(
        description=(
            "İlanın zorunlu tuttuğu beceriler. Her madde kısa bir beceri adı olsun "
            "(1-3 kelime, örn. 'Python', 'RAG', 'REST APIs'). Diploma veya deneyim "
            "yılı ekleme. Örnek olarak sayılan araçların her birini ayrı madde yap "
            "(örn. 'LangChain', 'LangGraph'). İşin tanımında (sorumluluklar kısmında) "
            "geçen becerileri de dahil et."
        )
    )
    nice_to_have: list[str] = Field(
        description=(
            "İlanda tercih sebebi / artı olarak belirtilen beceriler. Her madde kısa "
            "bir beceri adı olsun (1-3 kelime). Diploma veya deneyim yılı ekleme. "
            "Örnek olarak sayılan araçların her birini ayrı madde yap."
        )
    )
    min_years_experience: int | None = None


class CandidateProfile(BaseModel):
    name: str
    skills: list[str]
    years_experience: int


class SkillMatch(BaseModel):
    job_skill: str
    status: Literal["var", "kısmen", "yok"] = Field(
        description=(
            "'var': profilde aynı beceri ya da onu açıkça kapsayan bir beceri var. "
            "'kısmen': profilde ilgili ama aynı olmayan bir beceri var; öğrenmesi "
            "kolay olur (örn. LangGraph biliyorsa LangChain 'kısmen'). "
            "'yok': profilde gerçekten ilgili bir beceri yok."
        )
    )
    matched_with: str | None  # profildeki hangi beceriyle eşleşti
    reason: str  # kısa gerekçe


class SkillComparison(BaseModel):
    matches: list[SkillMatch]


class StudyItem(BaseModel):
    skill: str
    priority: Literal["yüksek", "orta", "düşük"]
    why: str  # bu ilan için neden önemli
    first_step: str  # bugün yapılabilecek somut ilk adım


class StudyPlan(BaseModel):
    items: list[StudyItem]
