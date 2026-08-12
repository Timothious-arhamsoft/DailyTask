import { useState } from 'react'
import { registerUser, loginUser } from '../../../../api/auth'
import './signup.css'

export function Signup({ onLoginSuccess }) {
  const [username, setUsername] = useState('')
  const [email, setEmail]       = useState('')
  const [password, setPassword] = useState('')
  const [error, setError]       = useState('')
  const [loading, setLoading]   = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      await registerUser({ username, email, password })
      const data = await loginUser({ email, password })
      onLoginSuccess(data.access_token)

    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <form className="signup-form" onSubmit={handleSubmit}>
      <h2 className="signup-title">Create Account</h2>

      {error && <p className="signup-error">{error}</p>}

      <div className="form-group">
        <label htmlFor="signup-username">Username</label>
        <input
          id="signup-username"
          type="text"
          value={username}
          onChange={e => setUsername(e.target.value)}
          placeholder="Your username"
          required
          minLength={3}
          maxLength={50}
        />
      </div>

      <div className="form-group">
        <label htmlFor="signup-email">Email</label>
        <input
          id="signup-email"
          type="email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="you@example.com"
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="signup-password">Password</label>
        <input
          id="signup-password"
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder="minimum 8 characters"
          required
          minLength={8}
        />
      </div>

      <button
        id="signup-submit-btn"
        type="submit"
        className="signup-btn"
        disabled={loading}
      >
        {loading ? 'Creating account…' : 'Sign Up'}
      </button>
    </form>
  )
}
