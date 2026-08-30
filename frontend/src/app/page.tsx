'use client'

import { FormEvent, useState } from 'react'

type Seat = {
  program_id: string
  program_name: string
  total_seats: number
  available_seats: number
}

const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'

export default function Home() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [seats, setSeats] = useState<Seat[]>([])
  const [error, setError] = useState('')

  async function askCollexa(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const query = question.trim()
    if (!query) return
    setIsLoading(true)
    setError('')
    try {
      const response = await fetch(`${apiUrl}/api/chat/query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, session_id: crypto.randomUUID() }),
      })
      if (!response.ok) throw new Error('COLLEXA could not answer right now.')
      const data: { response: string } = await response.json()
      setAnswer(data.response)
    } catch (caughtError) {
      setError(caughtError instanceof Error ? caughtError.message : 'Something went wrong.')
    } finally {
      setIsLoading(false)
    }
  }

  async function loadSeats() {
    setError('')
    try {
      const response = await fetch(`${apiUrl}/api/seats/availability`)
      if (!response.ok) throw new Error('Seat availability is currently unavailable.')
      setSeats(await response.json() as Seat[])
    } catch (caughtError) {
      setError(caughtError instanceof Error ? caughtError.message : 'Something went wrong.')
    }
  }

  return (
    <main>
      <nav className="nav"><a href="#home" className="brand">KEC <span>COLLEXA</span></a><div><a href="#programs">Programs</a><a href="#admissions">Admissions</a><a href="#contact">Contact</a></div></nav>
      <section id="home" className="hero">
        <p className="eyebrow">Kathmandu Engineering College</p>
        <h1>Build your future in engineering.</h1>
        <p className="lede">Explore KEC programs, admission information, notices, and student services in one place.</p>
        <div className="actions"><a className="button" href="#admissions">Explore admissions</a><button className="button secondary" onClick={loadSeats}>Check seats</button></div>
      </section>
      <section id="programs" className="section"><p className="eyebrow">Academic programs</p><h2>Engineering disciplines at KEC</h2><div className="cards">{['Computer Engineering', 'Communication, Electronics and IT Engineering', 'Electrical Engineering', 'Architecture', 'Civil Engineering'].map((program) => <article className="card" key={program}><h3>{program}</h3><p>Explore the curriculum, practical learning opportunities, and admission information with COLLEXA.</p></article>)}</div></section>
      <section id="admissions" className="section split"><div><p className="eyebrow">Admissions</p><h2>Start with a verified answer.</h2><p>Ask COLLEXA about programs, eligibility, campus facilities, or the admission process. Private services require a student login.</p></div><form className="chat" onSubmit={askCollexa}><label htmlFor="question">Ask COLLEXA</label><textarea id="question" value={question} onChange={(event) => setQuestion(event.target.value)} placeholder="How do I apply to KEC?" rows={4}/><button className="button" disabled={isLoading}>{isLoading ? 'Thinking…' : 'Ask COLLEXA'}</button>{answer && <p className="answer">{answer}</p>}</form></section>
      {seats.length > 0 && <section className="section"><p className="eyebrow">Live availability</p><h2>Program seats</h2><div className="cards">{seats.map((seat) => <article className="card" key={seat.program_id}><h3>{seat.program_name}</h3><p><strong>{seat.available_seats}</strong> of {seat.total_seats} seats available</p></article>)}</div></section>}
      {error && <p className="error" role="alert">{error}</p>}
      <footer id="contact">KEC COLLEXA · Official answers are sourced from the approved knowledge base.</footer>
    </main>
  )
}
