import './About.css'

export function About () {
  return (
    <section className="about-section" id="about">
      <div className="about-container">
        <span className="about-badge">About Me</span>
        <h2 className="about-title">
          Hello, I am <span className="highlight">Timothious</span>
        </h2>
        <p className="about-description">
          I design and develop high-performance web apps, games, and intelligent
          systems combining full-stack engineering, Unity development, and AI to
          create seamless, real-world experiences.
        </p>
      </div>
    </section>
  )
}
