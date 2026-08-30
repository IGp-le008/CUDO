import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'COLLEXA | Kathmandu Engineering College',
  description: 'KEC information portal and student services',
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
