import React from 'react'
import './Skills.css'

export const Skills = () => {
  const skillsList = [
    'React.js & Full-Stack Web Engineering',
    'AI & Intelligent Systems Development',
    'Unity & Game Development',
    'JavaScript (ES6+) & TypeScript',
    'Python & Machine Learning',
    'RESTful APIs & Microservices',
    'HTML5, CSS3 & Responsive UI Design',
    'Git & Version Control'
  ]

  return (
    <section className="skills-section" id="skills">
      <div className="skills-container">
        <h2 className="skills-title">Skills</h2>
        <p className="skills-subtitle">Summary of my technical and professional skills.</p>
        
        <ul className="skills-list">
          {skillsList.map((skill, index) => {
            const formattedNum = String(index + 1).padStart(2, '0') + '.'
            return (
              <li key={index} className="skill-item">
                <span className="skill-number">{formattedNum}</span>
                <span className="skill-name">{skill}</span>
              </li>
            )
          })}
        </ul>
      </div>
    </section>
  )
}
