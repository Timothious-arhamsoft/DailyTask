import { Badge } from '../Badge'
import './Notes.css'

export function NoteCard({ note, isAdmin, currentUser, onEdit, onDelete }) {
  // Format the date
  const formattedDate = new Date(note.updated_at || note.created_at).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })

  // Helper to determine author username display
  const getAuthorLabel = () => {
    if (note.username) return note.username
    if (note.user_name) return note.user_name
    if (note.owner_name) return note.owner_name
    if (note.author) return note.author
    if (note.owner?.username) return note.owner.username
    if (note.owner?.name) return note.owner.name
    if (note.owner?.email) return note.owner.email.split('@')[0]

    const currentUserId = currentUser?.sub || currentUser?.id
    const currentUsername = currentUser?.username || currentUser?.name || (currentUser?.email ? currentUser.email.split('@')[0] : 'Admin')

    if (note.owner_id && currentUserId && String(note.owner_id) === String(currentUserId)) {
      return currentUsername
    }

    return note.username || 'User'
  }

  const authorName = getAuthorLabel()
  const currentUserId = currentUser?.sub || currentUser?.id
  const isSelf = note.owner_id && currentUserId && String(note.owner_id) === String(currentUserId)

  return (
    <div className="note-card" id={`note-card-${note.id}`}>
      <div className="note-card-header">
        <h3 className="note-title">{note.title}</h3>
        {isAdmin && (
          <Badge 
            label={isSelf ? 'Admin' : authorName} 
            variant={isSelf ? 'admin' : 'user'} 
            icon="👤" 
          />
        )}


      </div>
      <div className="note-card-body">
        <p className="note-body-text">{note.body}</p>
      </div>
      <div className="note-card-footer">
        <span className="note-date">{formattedDate}</span>
        <div className="note-card-actions">
          <button 
            className="note-btn edit-btn" 
            onClick={() => onEdit(note)}
            aria-label="Edit note"
          >
            Edit
          </button>
          <button 
            className="note-btn delete-btn" 
            onClick={() => onDelete(note.id)}
            aria-label="Delete note"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  )
}

