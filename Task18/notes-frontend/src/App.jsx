import { useState } from 'react'
import { Navbar, Footer } from './components/index.js'
import {Login, Home} from './pages/index.js'

function App() {
  const [token, setToken] = useState(null)

  function handleLoginSuccess(receivedToken) {
    setToken(receivedToken)
  }

  return (
    <div className="app-layout">
      <Navbar />

      {token ? (
        <Home token={token} onLogout={() => setToken(null)} />
      ) : (
        <Login onLoginSuccess={handleLoginSuccess} />
      )}

      <Footer />
    </div>
  )
}

export default App
