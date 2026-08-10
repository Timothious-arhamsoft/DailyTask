import { ProjectCard } from "../../components";
import projects from "../../data/projects.json";
import "./Projects.css";

export function Projects({ sectionTitle = "Projects" }) {
    return (
        <section className="projects-section" id="projects" aria-labelledby="projects-heading">
            <div className="projects-container">
                <h2 id="projects-heading" className="projects-title">{sectionTitle}</h2>
                <p className="projects-subtitle">
                    Here are some of my latest projects that showcase my skills and experience.
                </p>

                <div className="projects-grid">
                    {projects.map((project) => (
                        <ProjectCard
                            key={project.id}
                            title={project.title}
                            description={project.description}
                            technologies={project.technologies}
                            link={project.link}
                        />
                    ))}
                </div>
            </div>
        </section>
    )
}