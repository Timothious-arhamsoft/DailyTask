import { NoteCard } from './NoteCard'
import './Notes.css'

export function NoteList({ notes, onEdit, onDelete }) {
  if (notes.length === 0) {
    return (
      <div className="notes-empty">
        <p>No notes found. Create your first note above!</p>
      </div>
    )
  }

  return (
    <div className="notes-list-container">
      {notes.map((note) => (
        <NoteCard
          key={note.id} // using real key from database
          note={note}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  )
}
