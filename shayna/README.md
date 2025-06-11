# Simon Karuga Django Portfolio

Welcome to the Django portfolio website of **Simon Karuga** – Python Django Web Developer, UI/UX Designer, and Digital Solutions Expert.

---

## 🚀 Project Overview

This project is a modern, responsive, and feature-rich personal portfolio and business website built with Django. It showcases Simon Karuga’s skills, experience, services, and portfolio, and includes interactive sections, a contact form, and creative Three.js animated backgrounds for a stunning user experience.

---

## ✨ Features

- **Homepage:** Engaging hero section, animated stats, and navigation.
- **About:** Professional bio, skills, and personal info.
- **Resume:** Timeline of work experience and education, skills, and achievements.
- **Portfolio:** Gallery of projects with details and testimonials.
- **Services:** Detailed service offerings and call-to-action.
- **Contact:** Secure contact form with validation and email support.
- **Starter Page:** Clean template for rapid prototyping or new features.
- **Three.js Backgrounds:** Unique animated backgrounds for each major page.
- **Responsive Design:** Mobile-friendly and cross-browser compatible.
- **AOS Animations:** Smooth scroll and fade-in effects.
- **Social Links:** Quick access to all major social platforms.
- **SEO Optimized:** Meta tags and semantic HTML.

---

## 🛠️ Tech Stack

- **Backend:** Django 4.x, Python 3.x
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript (ES6+)
- **Animations:** [Three.js](https://threejs.org/), [AOS](https://michalsnik.github.io/aos/), [Lottie](https://lottiefiles.com/)
- **Forms:** Django Crispy Forms
- **Icons:** Bootstrap Icons
- **Deployment:** Ready for Heroku, DigitalOcean, or any VPS

---

## 📁 Project Structure

```
shayna/
├── assets/
│   ├── css/
│   ├── img/
│   ├── js/
│   └── vendor/
├── august/
│   ├── templates/
│   │   └── august/
│   │       ├── index.html
│   │       ├── about.html
│   │       ├── resume.html
│   │       ├── portfoliodetails.html
│   │       ├── servicedetails.html
│   │       ├── contact.html
│   │       └── starterpage.html
│   └── views.py
├── manage.py
└── ...
```

---

## ⚡ Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/simon-karuga-portfolio.git
   cd simon-karuga-portfolio
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Open in your browser:**
   ```
   http://127.0.0.1:8000/
   ```

---

## 🖼️ Screenshots

> _Add screenshots of your homepage, resume, portfolio, and contact page here for a visual preview._

---

## 📝 Customization

- **Static Files:** Place your images, CSS, and JS in the `assets/` directory.
- **Three.js Animations:** Each major page has its own unique Three.js background. You can customize these in the `<script>` blocks at the bottom of each template.
- **Navigation:** Update links and social profiles in the header/footer sections of each template.
- **Content:** Edit the HTML templates in `august/templates/august/` to update your bio, experience, services, and more.

---

## 📬 Contact

For questions, feedback, or collaboration, reach out via the [Contact page](http://127.0.0.1:8000/contact) or email **simonkaruga945@gmail.com**.

---

## 📄 License

This project is for personal and educational use. For commercial use or template redistribution, please contact the author.

---

**Designed & Developed by Simon Karuga**  
_Crafting Code, Building Solutions_