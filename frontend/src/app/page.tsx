'use client'

import { FormEvent, useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import {
  Navigation,
  HeroSection,
  ProgramCard,
  ChatWidget,
  AnimatedBackground,
} from '@/components'
import { BookOpen, Users, Zap, Building2, Landmark } from 'lucide-react'

type Seat = {
  program_id: string
  program_name: string
  total_seats: number
  available_seats: number
}

const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'

const PROGRAMS = [
  {
    id: 'civil',
    title: 'Civil Engineering',
    description: '4-year program focused on infrastructure, construction, and design.',
    icon: <Landmark size={24} />,
    seats: 60,
  },
  {
    id: 'computer',
    title: 'Computer Engineering',
    description: 'Master software development, algorithms, and computer systems.',
    icon: <BookOpen size={24} />,
    seats: 65,
  },
  {
    id: 'electrical',
    title: 'Electrical Engineering',
    description: 'Study power systems, electronics, and electrical design.',
    icon: <Zap size={24} />,
    seats: 50,
  },
  {
    id: 'architecture',
    title: 'Architecture',
    description: 'Design buildings and urban spaces with creativity and science.',
    icon: <Building2 size={24} />,
    seats: 55,
  },
  {
    id: 'electronics',
    title: 'Electronics & Communication',
    description: 'Learn telecommunications, signal processing, and modern electronics.',
    icon: <Users size={24} />,
    seats: 58,
  },
]

export default function Home() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [seats, setSeats] = useState<Seat[]>([])
  const [error, setError] = useState('')
  const [showSeats, setShowSeats] = useState(false)

  useEffect(() => {
    // Load seats on mount
    loadSeats()
  }, [])

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
      setSeats((await response.json()) as Seat[])
    } catch (caughtError) {
      setError(caughtError instanceof Error ? caughtError.message : 'Something went wrong.')
    }
  }

  return (
    <AnimatedBackground>
      <Navigation />
      <ChatWidget />

      {/* Hero Section */}
      <HeroSection />

      {/* Programs Section */}
      <section id="programs" className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center mb-16"
          >
            <p className="text-sm font-semibold text-primary-600 dark:text-primary-400 uppercase tracking-wide mb-4">
              Academic Excellence
            </p>
            <h2 className="text-4xl sm:text-5xl font-bold text-gray-900 dark:text-white mb-6">
              Engineering Programs
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
              Choose from our diverse range of engineering disciplines designed to prepare you for
              a successful career.
            </p>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {PROGRAMS.map((program, idx) => (
              <ProgramCard
                key={program.id}
                title={program.title}
                description={program.description}
                icon={program.icon}
                seats={program.seats}
                index={idx}
              />
            ))}
          </div>
        </div>
      </section>

      {/* Admissions Section */}
      <section id="admissions" className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50 dark:bg-gray-900/50">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            {/* Left Content */}
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
            >
              <p className="text-sm font-semibold text-primary-600 dark:text-primary-400 uppercase tracking-wide mb-4">
                Admission Process
              </p>
              <h2 className="text-4xl font-bold text-gray-900 dark:text-white mb-6">
                Start Your Journey at KEC
              </h2>
              <p className="text-lg text-gray-600 dark:text-gray-300 mb-8">
                Ask COLLEXA about programs, eligibility requirements, application process, and
                campus facilities. Our AI assistant is available 24/7 to answer your questions.
              </p>

              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => setShowSeats(!showSeats)}
                className="px-8 py-4 bg-gradient-to-r from-primary-600 to-primary-700 text-white rounded-lg font-semibold hover:shadow-lg hover:shadow-primary-600/50 transition-all"
              >
                {showSeats ? 'Hide Seat Availability' : 'Check Seat Availability'}
              </motion.button>
            </motion.div>

            {/* Right Form */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.8 }}
              className="bg-white dark:bg-dark-900 rounded-2xl p-8 border border-gray-200 dark:border-gray-800 shadow-lg"
            >
              <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
                Ask COLLEXA
              </h3>
              <form onSubmit={askCollexa} className="space-y-4">
                <div>
                  <label htmlFor="question" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                    Your Question
                  </label>
                  <textarea
                    id="question"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="E.g., What are the eligibility criteria for Computer Engineering?"
                    rows={4}
                    className="w-full px-4 py-3 bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 resize-none"
                  />
                </div>

                <motion.button
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                  disabled={isLoading}
                  type="submit"
                  className="w-full px-4 py-3 bg-gradient-to-r from-primary-600 to-primary-700 text-white rounded-lg font-semibold hover:shadow-lg hover:shadow-primary-600/50 disabled:opacity-50 transition-all"
                >
                  {isLoading ? 'Thinking...' : 'Ask COLLEXA'}
                </motion.button>

                {answer && (
                  <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mt-4 p-4 bg-primary-50 dark:bg-primary-950/30 border border-primary-200 dark:border-primary-800 rounded-lg"
                  >
                    <p className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                      COLLEXA's Response:
                    </p>
                    <p className="text-gray-800 dark:text-gray-200 whitespace-pre-wrap">{answer}</p>
                  </motion.div>
                )}
              </form>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Seats Availability Section */}
      {showSeats && seats.length > 0 && (
        <motion.section
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          id="seats"
          className="py-20 px-4 sm:px-6 lg:px-8"
        >
          <div className="max-w-7xl mx-auto">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8 }}
              className="text-center mb-16"
            >
              <p className="text-sm font-semibold text-primary-600 dark:text-primary-400 uppercase tracking-wide mb-4">
                Real-Time Information
              </p>
              <h2 className="text-4xl font-bold text-gray-900 dark:text-white">
                Available Seats for 2026
              </h2>
            </motion.div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {seats.map((seat, idx) => (
                <motion.div
                  key={seat.program_id}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: idx * 0.1 }}
                  className="bg-white dark:bg-dark-900 rounded-xl p-6 border border-gray-200 dark:border-gray-800 hover:shadow-lg transition-shadow"
                >
                  <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
                    {seat.program_name}
                  </h3>
                  <div className="space-y-3">
                    <div className="flex justify-between items-center">
                      <span className="text-gray-600 dark:text-gray-400">Total Capacity</span>
                      <span className="font-semibold text-gray-900 dark:text-white">
                        {seat.total_seats}
                      </span>
                    </div>
                    <div className="w-full bg-gray-200 dark:bg-gray-800 rounded-full h-2">
                      <div
                        className="bg-gradient-to-r from-primary-600 to-primary-700 h-2 rounded-full transition-all"
                        style={{
                          width: `${((seat.total_seats - seat.available_seats) / seat.total_seats) * 100}%`,
                        }}
                      />
                    </div>
                    <div className="flex justify-between items-center pt-2">
                      <span className="text-gray-600 dark:text-gray-400">Available</span>
                      <span className="text-lg font-bold text-primary-600 dark:text-primary-400">
                        {seat.available_seats} seats
                      </span>
                    </div>
                  </div>

                  <motion.button
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    className="w-full mt-4 px-4 py-2 border-2 border-primary-600 text-primary-600 dark:text-primary-400 rounded-lg font-semibold hover:bg-primary-50 dark:hover:bg-primary-950 transition-colors"
                  >
                    Reserve Seat
                  </motion.button>
                </motion.div>
              ))}
            </div>
          </div>
        </motion.section>
      )}

      {/* Error Display */}
      {error && (
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="fixed top-20 right-4 bg-red-50 dark:bg-red-950 border border-red-200 dark:border-red-800 text-red-600 dark:text-red-400 px-6 py-4 rounded-lg shadow-lg max-w-md"
          role="alert"
        >
          {error}
        </motion.div>
      )}

      {/* Footer */}
      <footer id="contact" className="border-t border-gray-200 dark:border-gray-800 py-12 px-4 sm:px-6 lg:px-8 bg-gray-50 dark:bg-gray-900/50">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div>
              <h3 className="font-bold text-lg text-gray-900 dark:text-white mb-4">COLLEXA</h3>
              <p className="text-gray-600 dark:text-gray-400">
                Your AI-powered college assistant at Kathmandu Engineering College.
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 dark:text-white mb-4">Quick Links</h4>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>
                  <a href="#programs" className="hover:text-primary-600 transition-colors">
                    Programs
                  </a>
                </li>
                <li>
                  <a href="#admissions" className="hover:text-primary-600 transition-colors">
                    Admissions
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 dark:text-white mb-4">Contact</h4>
              <p className="text-gray-600 dark:text-gray-400 text-sm">
                Email: admissions@kec.edu.np
                <br />
                Phone: +977-1-XXXX-XXXX
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 dark:text-white mb-4">Follow Us</h4>
              <div className="flex gap-4 text-gray-600 dark:text-gray-400">
                <a href="#" className="hover:text-primary-600 transition-colors">
                  Twitter
                </a>
                <a href="#" className="hover:text-primary-600 transition-colors">
                  Facebook
                </a>
              </div>
            </div>
          </div>

          <div className="border-t border-gray-200 dark:border-gray-800 pt-8 text-center text-gray-600 dark:text-gray-400">
            <p>
              © 2026 Kathmandu Engineering College. Built with ❤️ using COLLEXA AI Assistant.
            </p>
          </div>
        </div>
      </footer>
    </AnimatedBackground>
  )
}
