# Day 17 — React Revision & Deeper Concepts

For Day 17, I focused on revising the React fundamentals practiced during the portfolio project and building a deeper understanding of how React components, data, rendering, events, and application structure work together.

## 1. React Rendering

Reviewed how React takes components and their current data and turns them into the UI displayed in the browser.

The important idea is that when relevant data changes, React can render the updated UI instead of manually manipulating every DOM element.

---

## 2. Virtual DOM

Learned the basic concept of the **Virtual DOM** and how React uses its representation of the UI to determine what needs to change in the actual browser DOM.

This helps explain why React applications can update specific parts of the interface efficiently instead of rebuilding the entire page manually.

---

## 3. One-Way Data Flow

Reviewed React's **one-way data flow**, where data generally moves from a parent component to a child component through props.

For example, in the portfolio:

```text
projects.json
     ↓
Projects
     ↓
ProjectCard
     ↓
props
```

This makes the direction of data easier to understand and helps keep components predictable.

---

## 4. Props vs State

Reviewed the difference between **props** and **state**.

* **Props** are values passed from a parent component to a child component.
* **State** is data managed by a component that can change over time.
* Props are generally read-only from the receiving component's perspective.
* State changes can cause a component to render again with updated information.

This distinction is important for understanding the next stage of React development.

---

## 5. React Events

Learned how React handles browser events using event handler props such as:

```jsx
onClick
onChange
onSubmit
```

React event handlers allow components to respond to user interactions without directly attaching traditional DOM event listeners.

---

## 6. Event Object

Reviewed that event handlers can receive an event object containing information about the event.

For example:

```jsx
function handleSubmit(event) {
  event.preventDefault();
}
```

The event object can be used to control the default browser behavior and access information about the interaction.

---

## 7. Conditional Rendering

Learned that React can use normal JavaScript conditions to decide what should be displayed.

For example:

```jsx
{isLoggedIn ? <Dashboard /> : <Login />}
```

This concept is useful for displaying different UI based on application state or user actions.

---

## 8. Controlled and Uncontrolled Forms

Reviewed the difference between controlled and uncontrolled form elements.

A **controlled form** keeps the input value in React state, while an **uncontrolled form** allows the DOM itself to manage the current value.

The portfolio contact form currently makes use of native browser validation, while controlled forms are an important concept for future React form development.

---

## 9. Component Responsibility

Reviewed the importance of giving components a clear responsibility.

For example:

* `Navbar` → navigation
* `ProjectCard` → displaying one project
* `Notification` → displaying user feedback
* `Hero` → introductory section
* `Contact` → contact-related functionality

Keeping responsibilities separated makes components easier to understand, test, reuse, and maintain.

---

## 10. Component Import and Export

Reviewed how React components are shared between files using JavaScript modules.

For example:

```jsx
export default ProjectCard;
```

and then:

```jsx
import ProjectCard from "./ProjectCard";
```

The project's `index.js` files can also be used as centralized export points, making imports cleaner when working with multiple components.

---
