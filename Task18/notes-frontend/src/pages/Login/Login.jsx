import { useState } from 'react'
import { Signin, Signup } from './components/index.js'
import './Login.css'

export function Login({ onLoginSuccess }) {
  const [mode, setMode] = useState('signin') // 'signin' | 'signup'

  return (
    <main className="login-page">
      <div className="login-card">
        <div className="login-header">
          <span className="login-icon">📝</span>
          <h1 className="login-heading">Notes App</h1>
          <p className="login-sub">
            {mode === 'signin' ? 'Sign in to manage your notes' : 'Create a new account'}
          </p>
        </div>

        {mode === 'signin' ? (
          <Signin onLoginSuccess={onLoginSuccess} />
        ) : (
          <Signup onLoginSuccess={onLoginSuccess} />
        )}

        <div className="login-switch">
          {mode === 'signin' ? (
            <>Don't have an account? <button onClick={() => setMode('signup')}>Sign Up</button></>
          ) : (
            <>Already have an account? <button onClick={() => setMode('signin')}>Sign In</button></>
          )}
        </div>
      </div>
    </main>
  )
}
