import { useState } from 'react'
import './Navbar.css'

export function Navbar() {
    const [isOpen, setIsOpen] = useState(false)

    return (
        <nav className="navbar">
            <div className="navbar-container">
                <div className="navbar-brand">Notes App</div>
                <button 
                    className={`navbar-toggle ${isOpen ? 'active' : ''}`} 
                    onClick={() => setIsOpen(!isOpen)}
                    aria-label="Toggle menu"
                >
                    <span className="bar"></span>
                    <span className="bar"></span>
                    <span className="bar"></span>
                </button>

                <div className={`navbar-links ${isOpen ? 'open' : ''}`}>
                    <a href="#" className="navbar-link" onClick={() => setIsOpen(false)}>Home</a>
                    <a href="#" className="navbar-link" onClick={() => setIsOpen(false)}>About</a>
                    <a href="#" className="navbar-link" onClick={() => setIsOpen(false)}>Contact</a>
                </div>
            </div>
        </nav>
    )
}