import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Navbar, Footer } from './components'
import Home from './pages/Home/Home'
import Contact from './pages/Contact/Contact'
import './App.css'

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  )
}

export default App
