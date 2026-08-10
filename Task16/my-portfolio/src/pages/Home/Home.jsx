import { Hero, About, Skills } from './components'
import { Projects } from '../Projects/Projects'
export function Home() {
  return (
    <div className="home-page">
      <Hero />
      <About />
      <Skills />
      <Projects sectionTitle="Featured Projects" />
    </div>
  )
}


