import React from 'react'
import './About.css'

export function About() {
  return (
    <main className="about-page">
      <div className="about-container">
        <h1 className="about-title">About Notes App</h1>
        <p className="about-text">
          Notes App is a simple CRUD application for creating, editing, and
          managing your personal notes. It's built with a React frontend and
          a FastAPI backend, using JWT authentication to keep your notes
          private and secure.
        </p>
        <p className="about-text">
          You can create new notes, edit existing ones, and delete the ones
          you no longer need — all saved to a real database.
        </p>
      </div>
    </main>
  )
}