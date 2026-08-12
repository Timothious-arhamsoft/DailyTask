import './Notes.css'

export function NoteCard({ note, onEdit, onDelete }) {
  // Format the date
  const formattedDate = new Date(note.updated_at || note.created_at).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })

  return (
    <div className="note-card" id={`note-card-${note.id}`}>
      <div className="note-card-header">
        <h3 className="note-title">{note.title}</h3>
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
