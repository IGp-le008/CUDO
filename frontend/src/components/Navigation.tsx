'use client'

import React from 'react'
import { motion } from 'framer-motion'

interface NavigationProps {
  // Optional: for future use with page tracking
}

export const Navigation: React.FC<NavigationProps> = () => {
  const navItems = [
    { label: 'Programs', href: '#programs', id: 'programs' },
    { label: 'Admissions', href: '#admissions', id: 'admissions' },
    { label: 'Services', href: '#services', id: 'services' },
    { label: 'Contact', href: '#contact', id: 'contact' },
  ]

  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.5 }}
      className="sticky top-0 z-50 bg-gradient-to-r from-kec-primary-50 to-kec-secondary-50 dark:from-slate-warm-900 dark:to-slate-warm-800 backdrop-blur-md border-b-2 border-kec-primary-300 dark:border-kec-primary-700 shadow-lg"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        {/* Logo */}
        <motion.div
          whileHover={{ scale: 1.05 }}
          className="flex items-center gap-2 font-bold text-2xl"
        >
          <div className="w-8 h-8 bg-gradient-to-br from-kec-primary-600 to-kec-secondary-600 rounded-lg shadow-md" />
          <span className="hidden sm:inline text-kec-secondary-800 dark:text-slate-warm-100">KEC</span>
          <span className="text-kec-accent-700 dark:text-kec-accent-300 ml-1 font-bold">COLLEXA</span>
        </motion.div>

        {/* Desktop Navigation */}
        <div className="hidden md:flex items-center gap-8">
          {navItems.map((item) => (
            <motion.a
              key={item.id}
              href={item.href}
              whileHover={{ color: '#b8915b' }}
              className="text-kec-secondary-700 dark:text-slate-warm-200 transition-colors hover:text-kec-primary-700 font-medium"
            >
              {item.label}
            </motion.a>
          ))}
        </div>

        {/* Auth Buttons */}
        <div className="flex items-center gap-4">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="px-4 py-2 text-sm font-medium text-kec-secondary-700 dark:text-slate-warm-200 hover:bg-kec-primary-100 dark:hover:bg-slate-warm-700 rounded-lg transition-colors"
          >
            Login
          </motion.button>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="px-4 py-2 text-sm font-medium bg-gradient-to-r from-kec-primary-600 to-kec-primary-700 text-white rounded-lg hover:shadow-lg transition-all"
          >
            Register
          </motion.button>
        </div>
      </div>
    </motion.nav>
  )
}
