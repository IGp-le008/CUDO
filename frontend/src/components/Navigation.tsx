'use client'

import React from 'react'
import { motion } from 'framer-motion'

interface NavigationProps {
  currentPage?: string
}

export const Navigation: React.FC<NavigationProps> = ({ currentPage }) => {
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
      className="sticky top-0 z-50 bg-white/80 dark:bg-dark-900/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-800"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        {/* Logo */}
        <motion.div
          whileHover={{ scale: 1.05 }}
          className="flex items-center gap-2 font-bold text-2xl"
        >
          <div className="w-8 h-8 bg-gradient-to-br from-primary-500 to-secondary-500 rounded-lg" />
          <span className="hidden sm:inline">KEC</span>
          <span className="text-primary-600 dark:text-primary-400 ml-1">COLLEXA</span>
        </motion.div>

        {/* Desktop Navigation */}
        <div className="hidden md:flex items-center gap-8">
          {navItems.map((item) => (
            <motion.a
              key={item.id}
              href={item.href}
              whileHover={{ color: '#3b82f6' }}
              className="text-gray-700 dark:text-gray-300 transition-colors hover:text-primary-600"
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
            className="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"
          >
            Login
          </motion.button>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="px-4 py-2 text-sm font-medium bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
          >
            Register
          </motion.button>
        </div>
      </div>
    </motion.nav>
  )
}
