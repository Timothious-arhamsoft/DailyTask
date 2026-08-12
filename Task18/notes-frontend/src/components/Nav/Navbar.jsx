import { useState } from 'react'
import './Navbar.css'

export function Navbar({ currentPage, onNavigate }) {
    const [isOpen, setIsOpen] = useState(false)

    const handleNavigate = (e, page) => {
        e.preventDefault()
        if (onNavigate) {
            onNavigate(page)
        }
        setIsOpen(false)
    }

    return (
        <nav className="navbar">
            <div className="navbar-container">
                <div 
                    className="navbar-brand" 
                    onClick={(e) => handleNavigate(e, 'home')}
                    style={{ cursor: 'pointer' }}
                >
                    Notes App
                </div>
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
                    <button 
                        className={`navbar-link ${currentPage === 'home' ? 'active' : ''}`} 
                        onClick={(e) => handleNavigate(e, 'home')}
                    >
                        Home
                    </button>
                    <button 
                        className={`navbar-link ${currentPage === 'about' ? 'active' : ''}`} 
                        onClick={(e) => handleNavigate(e, 'about')}
                    >
                        About
                    </button>
                    <button 
                        className={`navbar-link ${currentPage === 'contact' ? 'active' : ''}`} 
                        onClick={(e) => handleNavigate(e, 'contact')}
                    >
                        Contact
                    </button>
                </div>
            </div>
        </nav>
    )
}