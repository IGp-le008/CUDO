'use client'

import React, { useEffect, useState } from 'react'
import { motion, useScroll, useTransform } from 'framer-motion'

export const HeroSection: React.FC = () => {
  const [isLoaded, setIsLoaded] = useState(false)
  const { scrollY } = useScroll()
  const droneY = useTransform(scrollY, [0, 400], [0, 200])
  const droneScale = useTransform(scrollY, [0, 400], [1, 0.6])
  const droneOpacity = useTransform(scrollY, [0, 500], [1, 0])

  useEffect(() => {
    setIsLoaded(true)
  }, [])

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.15,
        delayChildren: 0.3,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 30 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.8, ease: 'easeOut' },
    },
  }

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden pt-16 pb-20">
      {/* Background Gradient - Warm Professional */}
      <div className="absolute inset-0 -z-10 bg-gradient-elegant">
        <motion.div
          animate={{
            scale: [1, 1.05, 1],
            opacity: [0.4, 0.6, 0.4],
          }}
          transition={{ duration: 20, repeat: Infinity }}
          className="absolute top-1/4 left-1/4 w-96 h-96 bg-kec-primary-500 rounded-full mix-blend-multiply filter blur-3xl opacity-20"
        />
        <motion.div
          animate={{
            scale: [1, 0.95, 1],
            opacity: [0.3, 0.5, 0.3],
          }}
          transition={{ duration: 25, repeat: Infinity, delay: 2 }}
          className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-kec-accent-500 rounded-full mix-blend-multiply filter blur-3xl opacity-15"
        />
      </div>

      {/* Animated Drone - Flying down on load then follows scroll */}
      {isLoaded && (
        <>
          {/* Initial drone flight down */}
          <motion.div
            initial={{ opacity: 0, y: -200, x: 100 }}
            animate={{ opacity: 1, y: 0, x: 0 }}
            transition={{ duration: 2, ease: 'easeOut' }}
            className="absolute top-20 right-1/4 z-30"
          >
            <DroneIcon />
          </motion.div>

          {/* Drone that follows scroll */}
          <motion.div
            style={{
              y: droneY,
              scale: droneScale,
              opacity: droneOpacity,
            }}
            className="absolute top-20 right-1/4 z-20"
          >
            <DroneIcon size="small" />
          </motion.div>
        </>
      )}

      {/* Main Content */}
      <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <motion.div variants={containerVariants} initial="hidden" animate={isLoaded ? 'visible' : 'hidden'}>
          {/* Eyebrow */}
          <motion.p
            variants={itemVariants}
            className="text-sm font-semibold text-kec-primary-700 dark:text-kec-primary-300 uppercase tracking-widest mb-6"
          >
            ✈️ Welcome to KEC
          </motion.p>

          {/* Main Headline - Professional Warm Tones */}
          <motion.h1 variants={itemVariants} className="text-6xl sm:text-7xl lg:text-8xl font-bold tracking-tight mb-6">
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-kec-primary-700 via-kec-secondary-600 to-kec-accent-700">
              Build Your Future
            </span>
            <br />
            <span className="text-kec-secondary-800 dark:text-slate-warm-100">in Engineering</span>
          </motion.h1>

          {/* Subheading */}
          <motion.p
            variants={itemVariants}
            className="text-xl sm:text-2xl text-kec-secondary-700 dark:text-slate-warm-200 mb-10 max-w-3xl mx-auto leading-relaxed font-medium"
          >
            Experience world-class engineering education at Kathmandu Engineering College. Let COLLEXA guide you through programs, admissions, and campus life.
          </motion.p>

          {/* CTA Buttons */}
          <motion.div variants={itemVariants} className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-8">
            <motion.button
              whileHover={{ scale: 1.05, boxShadow: '0 20px 40px rgba(212, 165, 116, 0.3)' }}
              whileTap={{ scale: 0.98 }}
              className="px-8 py-4 bg-gradient-to-r from-kec-primary-600 to-kec-primary-700 text-white rounded-lg font-semibold hover:shadow-xl transition-all"
            >
              Explore Programs
            </motion.button>
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.98 }}
              className="px-8 py-4 border-2 border-kec-accent-600 text-kec-accent-700 dark:text-kec-accent-300 dark:border-kec-accent-400 rounded-lg font-semibold hover:bg-kec-accent-50 dark:hover:bg-kec-accent-950 transition-colors"
            >
              Ask COLLEXA
            </motion.button>
          </motion.div>

          {/* Scroll Indicator */}
          <motion.div
            variants={itemVariants}
            className="mt-16 flex justify-center"
            animate={{ y: [0, 8, 0] }}
            transition={{ duration: 2.5, repeat: Infinity }}
          >
            <svg className="w-6 h-6 text-kec-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
            </svg>
          </motion.div>
        </motion.div>
      </div>
    </section>
  )
}

// Drone Icon Component
const DroneIcon: React.FC<{ size?: 'normal' | 'small' }> = ({ size = 'normal' }) => {
  const sizeClass = size === 'small' ? 'w-12 h-12' : 'w-16 h-16'

  return (
    <motion.svg
      className={`${sizeClass} text-kec-accent-600`}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={1.5}
      animate={{ rotateZ: [0, 5, -5, 0] }}
      transition={{ duration: 4, repeat: Infinity }}
    >
      {/* Drone body */}
      <circle cx="12" cy="12" r="4" fill="currentColor" />
      {/* Arms */}
      <line x1="8" y1="12" x2="4" y2="12" />
      <line x1="16" y1="12" x2="20" y2="12" />
      <line x1="12" y1="8" x2="12" y2="4" />
      <line x1="12" y1="16" x2="12" y2="20" />
      {/* Propellers */}
      <circle cx="4" cy="12" r="2" fill="currentColor" opacity={0.6} />
      <circle cx="20" cy="12" r="2" fill="currentColor" opacity={0.6} />
      <circle cx="12" cy="4" r="2" fill="currentColor" opacity={0.6} />
      <circle cx="12" cy="20" r="2" fill="currentColor" opacity={0.6} />
    </motion.svg>
  )
}
