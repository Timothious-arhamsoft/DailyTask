import { useState } from 'react'
import { Notification } from '../Notification/Notification'
import './Contact.css'

export function Contact() {
  const [submitted, setSubmitted] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    setSubmitted(true)
    setTimeout(() => {
      setSubmitted(false)
    }, 5000)
  }

  return (
    <section id="contact" className="contact-section" aria-labelledby="contact-heading">
      <div className="contact-container">
        <h2 id="contact-heading" className="contact-title">Contact Me</h2>
        <p className="contact-subtitle">
          Have a question or want to work together? Send me a message below!
        </p>

        {submitted && (
          <Notification
            message="Thank you! Your message has been sent successfully."
            type="success"
          />
        )}

        <form onSubmit={handleSubmit} className="contact-form">
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              placeholder="Your full name"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder="your.email@example.com"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="subject">Subject</label>
            <select id="subject" name="subject" required>
              <option value="">Select a subject</option>
              <option value="project">Project inquiry</option>
              <option value="job">Job opportunity</option>
              <option value="general">General question</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              name="message"
              rows="6"
              placeholder="Write your message here..."
              minLength={10}
              required
            ></textarea>
          </div>

          <div className="form-group checkbox-group">
            <label htmlFor="updates" className="checkbox-label">
              <input
                type="checkbox"
                id="updates"
                name="updates"
              />
              I would like to receive updates.
            </label>
          </div>

          <fieldset className="form-fieldset">
            <legend>Preferred contact method</legend>

            <div className="radio-group">
              <label htmlFor="contact-email" className="radio-label">
                <input
                  type="radio"
                  id="contact-email"
                  name="contact-method"
                  value="email"
                  required
                />
                Email
              </label>

              <label htmlFor="contact-phone" className="radio-label">
                <input
                  type="radio"
                  id="contact-phone"
                  name="contact-method"
                  value="phone"
                />
                Phone
              </label>

              <label htmlFor="contact-message" className="radio-label">
                <input
                  type="radio"
                  id="contact-message"
                  name="contact-method"
                  value="message"
                />
                Message
              </label>
            </div>
          </fieldset>

          <button type="submit" className="btn-submit">
            Send Message
          </button>
        </form>
      </div>
    </section>
  )
}
