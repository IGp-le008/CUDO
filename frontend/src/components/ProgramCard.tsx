'use client'

import React from 'react'
import { motion } from 'framer-motion'
import { ArrowRight } from 'lucide-react'

interface ProgramCardProps {
  title: string
  description: string
  seats?: number
  icon?: React.ReactNode
  index?: number
}

export const ProgramCard: React.FC<ProgramCardProps> = ({
  title,
  description,
  seats,
  icon,
  index = 0,
}) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: index * 0.1 }}
      whileHover={{ y: -8, transition: { duration: 0.3 } }}
      className="group relative h-full"
    >
      <div className="absolute inset-0 bg-gradient-to-br from-primary-600/10 to-secondary-600/10 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

      <div className="relative h-full p-6 sm:p-8 border border-gray-200 dark:border-gray-800 rounded-2xl hover:border-primary-500/50 dark:hover:border-primary-500/50 transition-colors duration-300 flex flex-col">
        {/* Icon */}
        {icon && (
          <div className="w-12 h-12 bg-gradient-to-br from-primary-500 to-secondary-500 rounded-xl flex items-center justify-center text-white mb-4 group-hover:scale-110 transition-transform duration-300">
            {icon}
          </div>
        )}

        {/* Content */}
        <h3 className="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white mb-2">
          {title}
        </h3>
        <p className="text-gray-600 dark:text-gray-400 mb-4 flex-grow">
          {description}
        </p>

        {/* Seats Info */}
        {seats !== undefined && (
          <div className="mb-4 p-3 bg-primary-50 dark:bg-primary-950/30 rounded-lg">
            <p className="text-sm font-semibold text-primary-600 dark:text-primary-400">
              {seats} seats available
            </p>
          </div>
        )}

        {/* CTA */}
        <motion.button
          whileHover={{ gap: 8 }}
          className="inline-flex items-center gap-2 text-primary-600 dark:text-primary-400 font-semibold group/btn hover:text-primary-700 dark:hover:text-primary-300 transition-colors"
        >
          Learn more
          <ArrowRight size={18} className="group-hover/btn:translate-x-2 transition-transform" />
        </motion.button>
      </div>
    </motion.div>
  )
}
