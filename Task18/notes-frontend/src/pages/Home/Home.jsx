import React, { useState, useEffect } from 'react'
import { fetchNotes, fetchAllNotesAdmin, createNote, updateNote, deleteNote } from '../../api/notes'
import { NoteForm, NoteList } from '../../components/index.js'
import './Home.css'

function decodeToken(token) {
  try {
    const payload = token.split('.')[1]
    const json = atob(payload.replace(/-/g, '+').replace(/_/g, '/'))
    return JSON.parse(json)
  } catch {
    return null
  }
}


export default function Home({ token, user, onLogout }) {
  const [notes, setNotes] = useState([])
  const [loading, setLoading] = useState(true)
  const [noteBeingEdited, setNoteBeingEdited] = useState(null)
  const [showCreateForm, setShowCreateForm] = useState(false)
  const [feedback, setFeedback] = useState(null)

  const decoded = user || decodeToken(token)
  const isAdmin = decoded?.role === 'admin'
  console.log('decoded token payload:', decoded)
  console.log('isAdmin:', isAdmin)

  
  // Fetch all notes on component mount
  useEffect(() => {
    loadNotes()
  }, [])

  const loadNotes = async () => {
    setLoading(true)
    setFeedback(null)
    try {
      let data
      if (isAdmin) {
        try {
          data = await fetchAllNotesAdmin(token)
        } catch (adminErr) {
          if (adminErr.message.includes('403') || adminErr.message.includes('401')) {
            data = await fetchNotes(token)
          } else {
            throw adminErr
          }
        }
      } else {
        data = await fetchNotes(token)
      }
      setNotes(data)
    } catch (err) {
      setFeedback({
        status: err.message.includes('401') ? 401 : 500,
        message: `Failed to load notes: ${err.message}`,
        type: 'error'
      })
      if (err.message.includes('401') && onLogout) {
        setTimeout(() => onLogout(), 2000)
      }
    } finally {
      setLoading(false)
    }
  }

  // Create Note Handler (201 status code)
  const handleCreate = async (noteData) => {
    setFeedback(null)
    try {
      const response = await createNote(token, noteData)
      let newNote = response.data

      // Ensure owner_id is set so badge displays correctly for admin immediately
      if (!newNote.owner_id && (decoded?.sub || decoded?.id)) {
        newNote = { ...newNote, owner_id: decoded.sub || decoded.id }
      }
      
      // Update local state directly without refetching the whole list
      setNotes((prevNotes) => [newNote, ...prevNotes])
      setShowCreateForm(false)
      
      setFeedback({
        status: response.status,
        message: `Note created successfully! Status code: ${response.status} (Created)`,
        type: 'success'
      })
    } catch (err) {
      setFeedback({
        status: 400,
        message: `Create failed: ${err.message}`,
        type: 'error'
      })
    }
  }

  // Update Note Handler (200 status code)
  const handleUpdate = async (noteData) => {
    if (!noteBeingEdited) return
    setFeedback(null)
    try {
      const response = await updateNote(token, noteBeingEdited.id, noteData)
      const updatedNote = response.data

      // Update the specific note locally in state without refetching the whole list
      setNotes((prevNotes) =>
        prevNotes.map((n) => (n.id === updatedNote.id ? { ...n, ...updatedNote } : n))
      )
      setNoteBeingEdited(null)

      setFeedback({
        status: response.status,
        message: `Note updated successfully! Status code: ${response.status} (OK)`,
        type: 'success'
      })
    } catch (err) {
      const is404 = err.message.includes('404')
      setFeedback({
        status: is404 ? 404 : 400,
        message: is404 
          ? 'Error: Note no longer exists on the server! Status code: 404 (Not Found)' 
          : `Update failed: ${err.message}`,
        type: 'error'
      })
      if (is404) {
        // Remove it locally if it is gone
        setNotes((prevNotes) => prevNotes.filter((n) => n.id !== noteBeingEdited.id))
        setNoteBeingEdited(null)
      }
    }
  }

  // Delete Note Handler (204 status code)
  const handleDelete = async (id) => {
    // Confirmation dialog
    const confirmDelete = window.confirm('Are you sure you want to delete this note?')
    if (!confirmDelete) return

    setFeedback(null)
    try {
      const response = await deleteNote(token, id)
      
      // Update local state directly without refetching the whole list
      setNotes((prevNotes) => prevNotes.filter((n) => n.id !== id))
      
      setFeedback({
        status: response.status,
        message: `Note deleted successfully! Status code: ${response.status} (No Content)`,
        type: 'success'
      })
    } catch (err) {
      const is404 = err.message.includes('404')
      setFeedback({
        status: is404 ? 404 : 400,
        message: is404 
          ? 'Error: Note was already deleted or doesn\'t exist! Status code: 404 (Not Found)' 
          : `Delete failed: ${err.message}`,
        type: 'error'
      })
      if (is404) {
        // Sync local state if already deleted
        setNotes((prevNotes) => prevNotes.filter((n) => n.id !== id))
      }
    }
  }


  return (
    <main className="home-dashboard">
      <div className="dashboard-container">
        
        {/* API Response Status Banner */}
        {feedback && (
          <div className={`status-banner-card ${feedback.type}`}>
            <div className="banner-details">
              <span className="badge-status">Status {feedback.status}</span>
              <span className="banner-text">{feedback.message}</span>
            </div>
            <button className="close-banner" onClick={() => setFeedback(null)} aria-label="Close message">
              &times;
            </button>
          </div>
        )}

        <div className="dashboard-header-row">
          <div className="title-section">
            <h2 className="dashboard-title">My Notes Dashboard</h2>
            <p className="dashboard-subtitle">Manage all your ideas in one clean dashboard.</p>
          </div>
          
          <div className="header-actions">
            <button 
              className="action-btn primary-btn"
              onClick={() => {
                setNoteBeingEdited(null)
                setShowCreateForm(!showCreateForm)
              }}
            >
              {showCreateForm ? 'Close Form' : 'Add Note'}
            </button>
            {onLogout && (
              <button 
                className="action-btn logout-btn"
                onClick={onLogout}
              >
                Sign Out
              </button>
            )}
          </div>
        </div>

        {/* Note Form for creation */}
        {showCreateForm && !noteBeingEdited && (
          <NoteForm 
            onSubmit={handleCreate} 
            onCancel={() => setShowCreateForm(false)} 
          />
        )}

        {/* Note Form for editing */}
        {noteBeingEdited && (
          <NoteForm 
            key={noteBeingEdited.id} 
            noteBeingEdited={noteBeingEdited}
            onSubmit={handleUpdate}
            onCancel={() => setNoteBeingEdited(null)}
          />
        )}

        {/* Note List display */}
        {loading ? (
          <div className="dashboard-loading">
            <div className="spinner-loader"></div>
            <p>Loading your notes...</p>
          </div>
        ) : (
          <NoteList 
            notes={notes}
            isAdmin={isAdmin}
            currentUser={decoded}
            onEdit={(note) => {
              setShowCreateForm(false)
              setNoteBeingEdited(note)
              window.scrollTo({ top: 0, behavior: 'smooth' })
            }}
            onDelete={handleDelete}
          />
        )}
      </div>
    </main>
  )
}
export { Home }

