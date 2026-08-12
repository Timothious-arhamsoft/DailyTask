const API_URL = import.meta.env.VITE_API_URL

// POST /api/v1/auth/login
// Returns: { access_token, token_type }
export async function loginUser({ email, password }) {
  const res = await fetch(`${API_URL}/api/v1/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  })

  if (!res.ok) {
    const data = await res.json().catch(() => ({}))
    throw new Error(data.detail || `Login failed (${res.status})`)
  }

  return res.json()
}

// POST /api/v1/users/
// Returns: { id, username, email, role }
export async function registerUser({ username, email, password }) {
  const res = await fetch(`${API_URL}/api/v1/users/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password }),
  })

  if (!res.ok) {
    const data = await res.json().catch(() => ({}))
    throw new Error(data.detail || `Registration failed (${res.status})`)
  }

  return res.json()
}
