import { useState } from 'react'
import { loginUser } from '../../../../api/auth'
import './signin.css'

export function Signin({ onLoginSuccess }) {
  const [email, setEmail]       = useState('')
  const [password, setPassword] = useState('')
  const [error, setError]       = useState('')
  const [loading, setLoading]   = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      const data = await loginUser({ email, password })
      onLoginSuccess(data.access_token)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <form className="signin-form" onSubmit={handleSubmit}>
      <h2 className="signin-title">Sign In</h2>

      {error && <p className="signin-error">{error}</p>}

      <div className="form-group">
        <label htmlFor="signin-email">Email</label>
        <input
          id="signin-email"
          type="email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder="you@example.com"
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="signin-password">Password</label>
        <input
          id="signin-password"
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder="••••••••"
          required
        />
      </div>

      <button
        id="signin-submit-btn"
        type="submit"
        className="signin-btn"
        disabled={loading}
      >
        {loading ? 'Signing in…' : 'Sign In'}
      </button>
    </form>
  )
}
