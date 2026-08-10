import './Notification.css'

export function Notification({ message, type = 'success' }) {
  if (!message) return null

  return (
    <div className={`notification-banner ${type}`} role="alert">
      <span className="notification-icon">
        {type === 'success' ? '✓' : 'ℹ'}
      </span>
      <span className="notification-message">{message}</span>
    </div>
  )
}
