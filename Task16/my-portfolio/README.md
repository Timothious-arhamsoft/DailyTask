# Timothious Gill — Portfolio

A responsive, high-performance portfolio website built with React and Vite following semantic HTML5 standards and dark/orange design aesthetics.

## Project Structure
- `src/components/`: Reusable UI components (`Navbar`, `Footer`, `Contact`, `ProjectCard`).
- `src/pages/`: Main page components (`Home`, `Projects`, `Contact`).
- `src/data/`: Structured JSON data (`projects.json`).

---

## Security & Architecture Notes

### Why Week 3's CSRF Lesson Applies Identically to React Forms

Cross-Site Request Forgery (CSRF) is an attack where a malicious website tricks a user's browser into performing unwanted actions on a trusted site where the user is currently authenticated.

1. **Browser & Protocol Level Mechanism**:
   CSRF vulnerability exists because **browsers automatically include session cookies** with cross-origin HTTP requests (e.g., standard HTML `<form method="post">` submissions or fetch requests).

2. **React Rendering vs. Network Transport**:
   Generating a form dynamically using a React component (`<form method="post">`) instead of writing plain HTML changes **only how the DOM is created on the client side**. Once the user clicks submit or the browser dispatches the request, the HTTP protocol and browser cookie handling operate **identically**.

3. **Key Takeaway**:
   React does **not** protect forms from CSRF attacks out of the box. Security relies on:
   - **Anti-CSRF Tokens** (Synchronizer Token Pattern).
   - **SameSite Cookie Attributes** (`SameSite=Strict` or `SameSite=Lax`).
   - **Header-based Authorization** (e.g., passing JWTs via `Authorization: Bearer <token>` headers instead of relying on ambient cookies).
