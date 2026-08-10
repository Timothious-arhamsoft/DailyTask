import { NavLink } from 'react-router-dom'
import './Navbar.css'

export function Navbar() {
  return (
    <header className="navbar-header">
      <div className="navbar-container">
        <NavLink to="/" className="navbar-logo">
          Portfolio<span className="logo-dot">.</span>
        </NavLink>

        <nav className="navbar-links">
          <NavLink
            to="/"
            className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}
          >
            Home
          </NavLink>
          <NavLink
            to="/projects"
            className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}
          >
            Projects
          </NavLink>
          <NavLink 
            to="/contact" 
            className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}
          >
            Contact
          </NavLink>
        </nav>

        <div className="navbar-action">
          <NavLink to="mailto:timothious.gill@arhamsoft.com" className="btn-orange">
            Work with Me
          </NavLink>
        </div>
      </div>
    </header>
  )
}


