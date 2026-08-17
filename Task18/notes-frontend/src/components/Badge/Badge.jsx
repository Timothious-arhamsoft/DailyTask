import React from 'react'
import './Badge.css'

export function Badge({ 
  label, 
  children, 
  variant = 'default', 
  icon = '👤', 
  className = '' 
}) {
  const content = label || children

  if (!content) return null

  return (
    <span className={`custom-badge badge-${variant} ${className}`}>
      {icon && <span className="badge-icon" aria-hidden="true">{icon}</span>}
      <span className="badge-label">{content}</span>
    </span>
  )
}
