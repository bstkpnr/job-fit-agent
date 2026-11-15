import { useState } from 'react'
import type { Priority, Report, SkillMatch, Status } from './types'

// reports/*.json → src/data/*.json. Yeni rapor eklemek için kod değişmez.
const files = import.meta.glob<Report>('./data/*.json', { eager: true, import: 'default' })

const reports = Object.entries(files)
  .map(([path, report]) => ({ id: path.replace('./data/', '').replace('.json', ''), report }))
  .sort((a, b) => a.report.job.company.localeCompare(b.report.job.company, 'tr'))

const STATUSES: Status[] = ['var', 'kısmen', 'yok']
const STATUS_TITLE: Record<Status, string> = { var: 'Var', kısmen: 'Kısmen', yok: 'Yok' }

// report.py'deki mantığın aynısı: nice_to_have adları küçük harfli küme
function split(report: Report) {
  const nice = new Set(report.job.nice_to_have.map((s) => s.toLowerCase()))
  const required: SkillMatch[] = []
  const extras: SkillMatch[] = []
  for (const m of report.comparison.matches) {
    ;(nice.has(m.job_skill.toLowerCase()) ? extras : required).push(m)
  }
  return { required, extras }
}

function counts(matches: SkillMatch[]) {
  const c: Record<Status, number> = { var: 0, kısmen: 0, yok: 0 }
  for (const m of matches) c[m.status]++
  return c
}

function Summary({ matches }: { matches: SkillMatch[] }) {
  const c = counts(matches)
  return (
    <span className="summary">
      {STATUSES.map((s, i) => (
        <span key={s}>
          {i > 0 && ' · '}
          <span className={`dot dot-${s}`} />
          {s} {c[s]}
        </span>
      ))}
    </span>
  )
}

function StatusBadge({ status }: { status: Status }) {
  return <span className={`badge badge-${status}`}>{status}</span>
}

function PriorityBadge({ priority }: { priority: Priority }) {
  return <span className={`badge prio-${priority}`}>{priority}</span>
}

function SkillRow({ m }: { m: SkillMatch }) {
  return (
    <li className="skill">
      <div className="skill-head">
        <StatusBadge status={m.status} />
        <strong>{m.job_skill}</strong>
        {m.matched_with && <span className="matched">← {m.matched_with}</span>}
      </div>
      <p className="reason">{m.reason}</p>
    </li>
  )
}

function Detail({ report }: { report: Report }) {
  const { job, plan } = report
  const { required, extras } = split(report)

  return (
    <article className="detail">
      <header className="detail-head">
        <p className="company">{job.company}</p>
        <h1>{job.title}</h1>
        <p className="meta">
          <Summary matches={required} />
          {job.min_years_experience != null && (
            <span className="years">· en az {job.min_years_experience} yıl</span>
          )}
        </p>
      </header>

      <section>
        <h2>Zorunlu beceriler</h2>
        <div className="groups">
          {STATUSES.map((s) => {
            const items = required.filter((m) => m.status === s)
            return (
              <div key={s} className="group">
                <h3>
                  {STATUS_TITLE[s]} <span className="count">{items.length}</span>
                </h3>
                {items.length === 0 ? (
                  <p className="empty">—</p>
                ) : (
                  <ul>
                    {items.map((m) => (
                      <SkillRow key={m.job_skill} m={m} />
                    ))}
                  </ul>
                )}
              </div>
            )
          })}
        </div>
      </section>

      <section>
        <h2>
          Artı beceriler <span className="count">{extras.length}</span>
        </h2>
        {extras.length === 0 ? (
          <p className="empty">İlanda artı beceri yok.</p>
        ) : (
          <ul className="extras">
            {extras.map((m) => (
              <SkillRow key={m.job_skill} m={m} />
            ))}
          </ul>
        )}
      </section>

      <section>
        <h2>Çalışma planı</h2>
        {plan === null || plan.items.length === 0 ? (
          <p className="empty">Eksik beceri yok, plana gerek yok.</p>
        ) : (
          <ol className="plan">
            {plan.items.map((item) => (
              <li key={item.skill}>
                <div className="skill-head">
                  <PriorityBadge priority={item.priority} />
                  <strong>{item.skill}</strong>
                </div>
                <p className="reason">{item.why}</p>
                <p className="step">
                  <span>İlk adım</span> {item.first_step}
                </p>
              </li>
            ))}
          </ol>
        )}
      </section>
    </article>
  )
}

export default function App() {
  const [selected, setSelected] = useState(reports[0]?.id)
  const current = reports.find((r) => r.id === selected)

  if (!current) return <p className="empty">reports/*.json bulunamadı.</p>

  return (
    <div className="layout">
      <aside className="sidebar">
        <p className="brand">job-fit-agent</p>

        {/* Mobilde: seçim alanı */}
        <select
          className="picker"
          value={selected}
          onChange={(e) => setSelected(e.target.value)}
          aria-label="İlan seç"
        >
          {reports.map(({ id, report }) => (
            <option key={id} value={id}>
              {report.job.company} — {report.job.title}
            </option>
          ))}
        </select>

        {/* Masaüstünde: kart listesi */}
        <ul className="cards">
          {reports.map(({ id, report }) => (
            <li key={id}>
              <button
                className={`card ${id === selected ? 'active' : ''}`}
                onClick={() => setSelected(id)}
              >
                <span className="card-title">{report.job.title}</span>
                <span className="card-company">{report.job.company}</span>
                <Summary matches={split(report).required} />
              </button>
            </li>
          ))}
        </ul>
      </aside>

      <main>
        <Detail report={current.report} />
      </main>
    </div>
  )
}
