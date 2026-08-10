import { useState } from 'react'
import { NavLink } from 'react-router-dom'
import './Navbar.css'

export function Navbar() {
  const [isOpen, setIsOpen] = useState(false)

  const toggleMenu = () => {
    setIsOpen(prev => !prev)
  }

  const closeMenu = () => {
    setIsOpen(false)
  }

  return (
    <header className="navbar-header">
      <div className="navbar-container">
        <NavLink to="/" className="navbar-logo" onClick={closeMenu}>
          Portfolio<span className="logo-dot">.</span>
        </NavLink>

        <button
          className={`hamburger-btn ${isOpen ? 'open' : ''}`}
          onClick={toggleMenu}
          aria-label="Toggle navigation menu"
          aria-expanded={isOpen}
        >
          <span className="hamburger-bar"></span>
          <span className="hamburger-bar"></span>
          <span className="hamburger-bar"></span>
        </button>

        <div className={`navbar-menu ${isOpen ? 'open' : ''}`}>
          <nav className="navbar-links">
            <NavLink
              to="/"
              className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}
              onClick={closeMenu}
            >
              Home
            </NavLink>
            <NavLink
              to="/projects"
              className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}
              onClick={closeMenu}
            >
              Projects
            </NavLink>
            <NavLink 
              to="/contact" 
              className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}
              onClick={closeMenu}
            >
              Contact
            </NavLink>
          </nav>

          <div className="navbar-action">
            <a 
              href="mailto:timothious.gill@arhamsoft.com" 
              className="btn-orange"
              onClick={closeMenu}
            >
              Work with Me
            </a>
          </div>
        </div>
      </div>
    </header>
  )
}
