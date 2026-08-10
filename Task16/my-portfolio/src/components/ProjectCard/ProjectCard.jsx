export function ProjectCard({ title, description, technologies, link }) {
  return (
    <article className="project-card">
      <div>
        <h3>{title}</h3>
        <p>{description}</p>
        <h4>Technologies</h4>
        <ul className="project-tech-list">
          {technologies.map((technology) => (
            <li key={technology} className="project-tech-item">
              {technology}
            </li>
          ))}
        </ul>
      </div>

      <a
        href={link}
        target="_blank"
        rel="noopener noreferrer"
        className="project-link"
      >
        View project on GitHub &rarr;
      </a>
    </article>
  );
}

