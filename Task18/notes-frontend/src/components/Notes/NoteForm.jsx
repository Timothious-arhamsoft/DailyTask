import { useState } from 'react'
import './Notes.css'

export function NoteForm({ onSubmit, noteBeingEdited, onCancel }) {
  // If editing, initialize state from the note's existing values, otherwise start empty.
  const [title, setTitle] = useState(noteBeingEdited ? noteBeingEdited.title : '')
  const [body, setBody] = useState(noteBeingEdited ? noteBeingEdited.body : '')
  const [error, setError] = useState('')

  const isEditing = !!noteBeingEdited

  const handleSubmit = (e) => {
    e.preventDefault()
    setError('')

    if (!title.trim()) {
      setError('Title is required')
      return
    }

    onSubmit({
      title: title.trim(),
      body: body.trim()
    })

    if (!isEditing) {
      setTitle('')
      setBody('')
    }
  }

  return (
    <form className="note-form" onSubmit={handleSubmit}>
      <h3 className="form-title">{isEditing ? 'Edit Note' : 'Create New Note'}</h3>
      
      {error && <div className="form-error">{error}</div>}

      <div className="form-group">
        <label htmlFor="note-title">Title</label>
        <input
          id="note-title"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter note title..."
          required
          maxLength={200}
        />
      </div>

      <div className="form-group">
        <label htmlFor="note-body">Body</label>
        <textarea
          id="note-body"
          value={body}
          onChange={(e) => setBody(e.target.value)}
          placeholder="Enter note content..."
          rows={5}
        />
      </div>

      <div className="form-actions">
        <button type="submit" className="submit-btn">
          {isEditing ? 'Save Changes' : 'Add Note'}
        </button>
        {onCancel && (
          <button type="button" className="cancel-btn" onClick={onCancel}>
            Cancel
          </button>
        )}
      </div>
    </form>
  )
}
