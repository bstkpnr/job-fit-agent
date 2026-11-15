// src/job_fit_agent/models.py ile birebir aynı alanlar

export type Status = 'var' | 'kısmen' | 'yok'
export type Priority = 'yüksek' | 'orta' | 'düşük'

export interface JobPosting {
  title: string
  company: string
  required_skills: string[]
  nice_to_have: string[]
  min_years_experience: number | null
}

export interface SkillMatch {
  job_skill: string
  status: Status
  matched_with: string | null
  reason: string
}

export interface SkillComparison {
  matches: SkillMatch[]
}

export interface StudyItem {
  skill: string
  priority: Priority
  why: string
  first_step: string
}

export interface StudyPlan {
  items: StudyItem[]
}

// graph.py'deki to_json çıktısı
export interface Report {
  job: JobPosting
  comparison: SkillComparison
  plan: StudyPlan | null
}
