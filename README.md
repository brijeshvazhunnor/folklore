# My Django App

This is a Django application that uses [`django-widget-tweaks`](https://pypi.org/project/django-widget-tweaks/) to easily customize form field rendering in templates.

## 🚀 Features

- Django-powered web application
- Customizable forms with `django-widget-tweaks`

## 📦 Requirements

- Python 3.8+
- Django 3.2–4.x
- `django-widget-tweaks` >= 1.4.12

## 🛠 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-django-app.git
   cd your-django-app
   ```
Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
Install dependencies:

```bash

pip install -r requirements.txt
```
```bash
python manage.py migrate
python manage.py runserver
```