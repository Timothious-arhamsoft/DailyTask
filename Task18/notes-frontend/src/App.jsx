import { useState } from 'react'
import { Navbar, Footer } from './components/index.js'
import { Login, Home, About, Contact } from './pages/index.js'

function decodeToken(token) {
  try {
    const payload = token.split('.')[1]
    return JSON.parse(atob(payload))
  } catch {
    return null
  }
}

function App() {
  const [token, setToken] = useState(null)
  const [currentPage, setCurrentPage] = useState('home')

  function handleLoginSuccess(receivedToken) {
    setToken(receivedToken)
  }

  const user = token ? decodeToken(token) : null

  const renderContent = () => {
    switch (currentPage) {
      case 'about':
        return <About />
      case 'contact':
        return <Contact />
      case 'home':
      default:
        return token ? (
          <Home token={token} user={user} onLogout={() => setToken(null)} />
        ) : (
          <Login onLoginSuccess={handleLoginSuccess} />
        )
    }
  }

  return (
    <div className="app-layout">
      <Navbar currentPage={currentPage} onNavigate={setCurrentPage} />
      {renderContent()}
      <Footer />
    </div>
  )
}

export default App