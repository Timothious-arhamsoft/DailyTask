import heroBg from '../../../../assets/hero-bg.jpg'
import './Hero.css'

export function Hero() {
  return (
    <section 
      className="hero-section"
      style={{ backgroundImage: `url(${heroBg})` }}
    >
      <div className="hero-overlay"></div>
      <div className="hero-content">
        <h1 className="hero-title">Timothious Gill</h1>
        <p className="hero-subtitle">AI Engineer</p>
      </div>
    </section>
  )
}
