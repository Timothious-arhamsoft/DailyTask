const API_URL = import.meta.env.VITE_API_URL

// GET /api/v1/notes/
// Returns: [{ id, title, body, owner_id, category_id, created_at, updated_at }, ...]
export async function fetchNotes(token) {
  const res = await fetch(`${API_URL}/api/v1/notes/`, {
    headers: { Authorization: `Bearer ${token}` },
  })

  if (!res.ok) {
    throw new Error(`Failed to load notes (${res.status})`)
  }

  return res.json()
}

// POST /api/v1/notes/
// Returns: { id, title, body, owner_id, ... }   
export async function createNote(token, { title, body }) {
  const res = await fetch(`${API_URL}/api/v1/notes/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ title, body }),
  })

  if (!res.ok) {
    const data = await res.json().catch(() => ({}))
    throw new Error(data.detail || `Create failed (${res.status})`)
  }

  return { status: res.status, data: await res.json() }
}

// PUT /api/v1/notes/:id
// Returns: { id, title, body, ... }
export async function updateNote(token, id, { title, body }) {
  const res = await fetch(`${API_URL}/api/v1/notes/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ title, body }),
  })

  if (!res.ok) {
    const data = await res.json().catch(() => ({}))
    throw new Error(data.detail || `Update failed (${res.status})`)
  }

  return { status: res.status, data: await res.json() }
}

// DELETE /api/v1/notes/:id
// Returns: nothing   
export async function deleteNote(token, id) {
  const res = await fetch(`${API_URL}/api/v1/notes/${id}`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${token}` },
  })

  if (!res.ok) {
    const data = await res.json().catch(() => ({}))
    throw new Error(data.detail || `Delete failed (${res.status})`)
  }

  return { status: res.status }
}
