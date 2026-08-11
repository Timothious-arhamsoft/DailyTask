# React Portfolio — Vite

A personal portfolio website built with **React and Vite** as part of my React learning and practical development work.

The project focuses on learning and applying React fundamentals such as **JSX, components, component composition, props, reusable components, JSON-based data, array mapping, forms, native validation, notifications, semantic HTML, accessibility, and basic CSRF considerations**.

---

## 📌 Project Overview

This project is structured as a component-based React application.

Instead of keeping the entire portfolio inside one large component, the application is divided into:

- **Pages** — represent major sections/pages of the portfolio.
- **Components** — contain reusable UI elements.
- **Data** — stores project information separately from the UI.
- **Assets** — contains images and other static resources.
- **CSS files** — keep styling organized according to components/pages.

This structure makes the application easier to understand, maintain, and extend as more React functionality is added.

---

## 🛠️ Technologies Used

- **React** — Used to create the user interface using reusable components.
- **Vite** — Used as the React development server and build tool.
- **JavaScript (ES6+)** — Used for application logic and data handling.
- **JSX** — Used to write UI markup inside JavaScript.
- **HTML5** — Used for semantic structure and accessible forms.
- **CSS3** — Used for styling components and pages.
- **JSON** — Used to store portfolio project data.
- **ESLint** — Used to maintain code quality and identify potential JavaScript/React issues.

---

# 📂 Project Structure

```text
my-portfolio/
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
├── public/
│   └── icon.png
│
├── README.md
│
├── src/
│   ├── App.css
│   ├── App.jsx
│   │
│   ├── assets/
│   │   └── hero-bg.jpg
│   │
│   ├── components/
│   │   ├── Contact/
│   │   │   ├── Contact.css
│   │   │   └── Contact.jsx
│   │   │
│   │   ├── Footer/
│   │   │   ├── Footer.css
│   │   │   └── Footer.jsx
│   │   │
│   │   ├── index.js
│   │   │
│   │   ├── Nav/
│   │   │   ├── Navbar.css
│   │   │   └── Navbar.jsx
│   │   │
│   │   ├── Notification/
│   │   │   ├── Notification.css
│   │   │   └── Notification.jsx
│   │   │
│   │   └── ProjectCard/
│   │       └── ProjectCard.jsx
│   │
│   ├── data/
│   │   └── projects.json
│   │
│   ├── index.css
│   ├── main.jsx
│   │
│   └── pages/
│       ├── Contact/
│       │   └── Contact.jsx
│       │
│       ├── Home/
│       │   ├── components/
│       │   │   ├── About/
│       │   │   │   ├── About.css
│       │   │   │   └── About.jsx
│       │   │   │
│       │   │   ├── Hero/
│       │   │   │   ├── Hero.css
│       │   │   │   └── Hero.jsx
│       │   │   │
│       │   │   ├── index.js
│       │   │   │
│       │   │   └── Skills/
│       │   │       ├── Skills.css
│       │   │       └── Skills.jsx
│       │   │
│       │   └── Home.jsx
│       │
│       ├── index.js
│       │
│       └── Projects/
│           ├── Projects.css
│           └── Projects.jsx
│
└── vite.config.js
```

---

# 🗂️ Folder and File Responsibilities

## `src/main.jsx`

The main entry point of the React application.

It connects the React application to the DOM and renders the root component.

Conceptually:

```text
main.jsx
   ↓
App.jsx
   ↓
Pages + Components
```

---

## `src/App.jsx`

Acts as the main application component.

It brings together the major parts of the portfolio and provides the overall application structure.

---

# 📄 Pages

The `src/pages` directory contains the major sections of the portfolio.

### `pages/Home`

The Home page contains its own smaller components:

```text
Home
├── Hero
├── About
└── Skills
```

This demonstrates **component composition**, where a larger page is constructed from smaller UI components.

### `pages/Projects`

Contains the Projects page responsible for displaying the portfolio projects.

The project information is supplied from the JSON data file and displayed using reusable project cards.

### `pages/Contact`

Contains the main Contact page and its contact form functionality.

---

# 🧩 Reusable Components

The `src/components` directory contains components that can be reused independently across the application.

### `Navbar`

Contains the navigation UI for moving between portfolio sections.

### `Footer`

Contains the common footer section of the website.

### `Contact`

Contains reusable contact-related UI.

### `ProjectCard`

A reusable component used to display individual project information.

Instead of manually writing the same project markup multiple times, the component receives different project information through **props**.

Example:

```jsx
<ProjectCard
  title={project.title}
  description={project.description}
/>
```

This demonstrates how React components can be made reusable through props.

### `Notification`

A reusable component used to display feedback such as a successful form submission.

The message and notification type can be supplied through props.

---

# 📊 Project Data

Project information is stored in:

```text
src/data/projects.json
```

Keeping project information in a separate JSON file helps separate **data from presentation**.

The React application can read the project data and dynamically render it.

This makes it easier to add or modify projects without changing the structure of the `ProjectCard` component.

---

# 🖼️ Assets

The `src/assets` directory contains application-specific assets.

Currently it contains:

```text
hero-bg.jpg
```

The image is used as part of the Hero section of the portfolio.

The `public` directory contains:

```text
icon.png
```

which can be used as a publicly accessible static asset.

---

# 🎨 Styling Structure

CSS is organized alongside the relevant component or page.

For example:

```text
Hero/
├── Hero.jsx
└── Hero.css
```

and:

```text
Projects/
├── Projects.jsx
└── Projects.css
```

This keeps component-specific styling close to the component it belongs to.

Global styling is handled through files such as:

```text
src/index.css
src/App.css
```

---

# 📚 React Concepts Practiced

## 1. React Fundamentals

Learned how React applications are built using reusable and composable components.

---

## 2. Vite

Learned how to create, run, and build a React application using Vite.

Development server:

```bash
npm run dev
```

Production build:

```bash
npm run build
```

---

## 3. JSX

Practiced writing HTML-like markup inside JavaScript using JSX.

Also learned JSX-specific syntax such as:

```jsx
className
```

instead of HTML's:

```html
class
```

and:

```jsx
htmlFor
```

instead of:

```html
for
```

---

## 4. Components

Created multiple React components and separated the application into smaller UI units.

Examples include:

- Navbar
- Hero
- About
- Skills
- Projects
- ProjectCard
- Contact
- Notification
- Footer

---

## 5. Component Composition

Practiced building larger pages from smaller components.

For example:

```text
Home
├── Hero
├── About
└── Skills
```

This keeps individual components focused on specific responsibilities.

---

## 6. Props

Learned how parent components pass information to child components.

Props were particularly useful for making `ProjectCard` reusable.

A single `ProjectCard` can receive different project information and render the appropriate content.

---

## 7. JSON Data

Created:

```text
src/data/projects.json
```

to store project information separately from the React UI.

This provides a cleaner separation between application data and presentation.

---

## 8. `.map()`

Used JavaScript's `.map()` method to iterate over project data and dynamically create multiple `ProjectCard` components.

Conceptually:

```jsx
projects.map((project) => (
  <ProjectCard
    key={project.id}
    {...project}
  />
))
```

---

## 9. React `key`

Learned why a unique `key` is required when rendering lists of React components.

Project IDs can be used as stable keys:

```jsx
key={project.id}
```

---

## 10. Forms

Created a Contact form using React and semantic HTML.

The form contains appropriately labelled input fields and provides a structured way for users to submit information.

---

## 11. Native Form Validation

Practiced browser-provided HTML validation using attributes such as:

```html
required
```

```html
type="email"
```

and:

```html
minLength
```

This allows basic validation without having to implement every validation rule manually in JavaScript.

---

## 12. Form Submission

Practiced handling form submission from a React component.

The submission flow works together with the browser's native validation.

---

## 13. Notification Component

Created a separate reusable `Notification` component to provide feedback after successful form submission.

This avoids duplicating notification markup inside the Contact component.

---

## 14. Semantic HTML

Practiced using meaningful HTML elements such as:

```html
<nav>
<section>
<article>
<form>
<footer>
```

Semantic HTML makes the structure easier for browsers, search engines, and assistive technologies to understand.

---

## 15. Accessibility

Practiced basic accessibility principles including:

- Proper form labels
- Correct heading structure
- Semantic HTML
- Keyboard-friendly interaction
- Meaningful links
- Accessible form controls

---

## 16. CSRF Concepts

Reviewed how CSRF considerations still apply to React applications.

React does not automatically remove browser-level security concerns. Applications using cookie-based authentication still need appropriate CSRF protection for state-changing requests.

---

# 💻 Practical Work Completed

During the project implementation, I completed the following:

- Created the React application using Vite.
- Organized the application into pages and reusable components.
- Created the Home page with Hero, About, and Skills sections.
- Created the Projects page.
- Created a reusable `ProjectCard` component.
- Created `projects.json` for project data.
- Used props to pass project information into `ProjectCard`.
- Used `.map()` to dynamically render project cards.
- Added unique keys to dynamically rendered components.
- Created a Contact page and contact form.
- Added native browser form validation.
- Created a reusable Notification component.
- Added semantic HTML elements.
- Practiced accessibility and keyboard navigation.
- Organized CSS files according to components and pages.
- Added portfolio assets such as the Hero background image.
- Verified the application using the Vite production build.

---

# 🧪 Testing and Verification

The application was tested using:

```bash
npm run dev
```

The production build was also verified using:

```bash
npm run build
```

The build completed successfully with **0 errors**.

---

# 📈 Current Architecture

The current application follows a structure similar to:

```text
App
│
├── Navbar
│
├── Home
│   ├── Hero
│   ├── About
│   └── Skills
│
├── Projects
│   └── ProjectCard
│
├── Contact
│   └── Notification
│
└── Footer
```

This structure demonstrates the basic React concept of building an interface through **composition of reusable components**.

---

## 🔗 Repository

GitHub:

`https://github.com/Timothious-arhamsoft/DailyTask/tree/dev/Task16/my-portfolio`