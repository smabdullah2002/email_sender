# 📧 Email Sender Web App

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.0-green?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple?logo=bootstrap)
![HTML5](https://img.shields.io/badge/HTML-5-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS-3-blue?logo=css3)

---

## 🚀 Overview

A simple and elegant email sender web application built using **Django**, **Python**, **Bootstrap**, **HTML**, and **CSS**.

Users can:
- Input recipient email address
- Enter a subject and message
- Send styled emails with ease

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Django
- **Email Service:** Django Email Backend (SMTP)

---

## 🧪 Features

- 📬 Send emails with subject and message
- ✅ Simple, clean Bootstrap-based UI
- 🔐 Backend handles all validation and SMTP logic

---

## 🔒 Configuration

In your `settings.py`, configure your SMTP settings like this:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'


