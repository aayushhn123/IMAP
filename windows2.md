# 🚀 Django End-to-End Website Setup Cheat Sheet

This guide will help you create and run a **demo Django website** from scratch — no missing template or setup errors.

---

## 🧩 1. Create & Activate Virtual Environment
```bash
# Create new folder and move into it
mkdir django_demo
cd django_demo

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate       # (Windows)
# OR
source venv/bin/activate    # (Mac/Linux)
```

---

## ⚙️ 2. Install Django
```bash
pip install django
```

---

## 🏗️ 3. Create Django Project
```bash
django-admin startproject mysite .
```

> The `.` at the end tells Django to create the project **in the current folder**.

Folder structure:
```
django_demo/
├── manage.py
└── mysite/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    ├── wsgi.py
```

---

## 🧱 4. Create an App
```bash
python manage.py startapp blog
```

Folder structure:
```
django_demo/
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│
└── blog/
    ├── views.py
    ├── urls.py   ✅ (create this)
    ├── templates/
    │   └── blog/
    │       └── home.html  ✅ (create this)
```

---

## 🧾 5. Add App to Settings
Edit `mysite/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # ✅ add this
]
```

Also ensure this in settings:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],      # leave blank
        'APP_DIRS': True,  # ✅ must be True
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

## 🌐 6. Set Up URLs

### `blog/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### `mysite/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

---

## 💻 7. Create View
`blog/views.py`:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')
```

---

## 🧱 8. Create Template
```
blog/
└── templates/
    └── blog/
        └── home.html
```

`home.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Django Demo</title>
</head>
<body>
    <h1>🎉 Welcome to My Django Demo Website!</h1>
    <p>This page is being served successfully by Django.</p>
</body>
</html>
```

---

## 🧩 9. Migrate Database
```bash
python manage.py migrate
```

---

## ⚙️ 10. Run Server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧼 Optional Extras

✅ Create a superuser:
```bash
python manage.py createsuperuser
```

✅ Admin panel:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

✅ Stop server:
```bash
Ctrl + C
```

---

## 🧠 Common Fixes

| Error | Cause | Fix |
|-------|--------|-----|
| `TemplateDoesNotExist` | Wrong folder structure | Make sure `app/templates/app/template.html` exists |
| `ModuleNotFoundError` | App not added in settings | Add app name in `INSTALLED_APPS` |
| `NameError` | Variable undefined in view | Define before using or remove |

---
