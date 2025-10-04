# Django Project Setup Cheat Sheet (Mac, VS Code)

This cheat sheet guides you through setting up a Django project on **macOS** using **VS Code**, adapted from the original "Django End-to-End Website Setup Cheat Sheet." It uses **Terminal** for Unix-like commands, Python 3.12+, and the standard `venv` module for virtual environments. Covers project setup, apps, URLs, templates, migrations, and Git integration.

## Prerequisites
- Install **Python** from [python.org](https://python.org) or using **Homebrew**:
  ```bash
  brew install python
  ```
- Install **Git** (usually preinstalled on macOS, but update via Homebrew if needed):
  ```bash
  brew install git
  ```
- Install **VS Code** from [code.visualstudio.com](https://code.visualstudio.com).
- Use **Terminal** for all commands (`ls`, `source`, etc.).
- Familiarize with commands: `cd` (change dir), `ls` (list files), `mkdir` (make dir).
- Open VS Code:  
  ```bash
  code .
  ```

---

## 1. Create Project Directory
- Create and navigate to a root directory:
  ```bash
  mkdir my-django-project
  cd my-django-project
  ```

- Open in VS Code:
  ```bash
  code .
  ```

---

## 2. Create & Activate Virtual Environment
- Create a virtual environment:
  ```bash
  python3 -m venv .venv
  ```

- Activate it in Terminal:
  ```bash
  source .venv/bin/activate
  ```

  Verify: Prompt shows `(.venv)`.  
  Deactivate with:
  ```bash
  deactivate
  ```

---

## 3. Install Django
- With the virtual environment active, install Django:
  ```bash
  pip install django
  ```

---

## 4. Initialize Git (Version Control)
- Initialize a Git repository:
  ```bash
  git init
  ```

- Create `.gitignore` in VS Code:
  ```gitignore
  # Python/Django
  *.pyc
  *.pyo
  __pycache__/
  .venv/
  db.sqlite3
  .env

  # Logs and temp
  *.log
  *.pot
  *.mo
  ```

- Stage and commit:
  ```bash
  git add .
  git commit -m "Initial project setup with venv and Git"
  ```

- **Check Status/History:**
  ```bash
  git status
  git log --oneline
  ```

- **Later (GitHub):** Create a repo on GitHub, then:
  ```bash
  git remote add origin <url>
  git push -u origin main
  ```

---

## 5. Start Django Project
- Run in project root (venv active; check dir with `ls`):
  ```bash
  django-admin startproject mysite .
  ```

- **Artifacts Created:**
  - `manage.py`: CLI for Django commands.
  - `mysite/` directory: Contains `settings.py`, `urls.py`, etc.

- Test setup:
  ```bash
  python3 manage.py runserver
  ```
  Visit `http://127.0.0.1:8000/` to see Django welcome page.

---

## 6. Create an App
- Create a Django app:
  ```bash
  python3 manage.py startapp blog
  ```

- Folder structure:
  ```
  my-django-project/
  ├── .venv/
  ├── manage.py
  ├── mysite/
  │   ├── settings.py
  │   ├── urls.py
  │   ├── asgi.py
  │   ├── wsgi.py
  ├── blog/
  │   ├── views.py
  │   ├── urls.py   # Create this
  │   ├── templates/
  │   │   └── blog/
  │   │       └── home.html  # Create this
  ```

---

## 7. Add App to Settings
- Edit `mysite/settings.py` in VS Code:
  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'blog',  # Add this
  ]
  ```

- Ensure template settings:
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],  # Leave blank
          'APP_DIRS': True,  # Must be True
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

## 8. Set Up URLs
- Create `blog/urls.py` in VS Code:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.home, name='home'),
  ]
  ```

- Edit `mysite/urls.py`:
  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('blog.urls')),
  ]
  ```

---

## 9. Create View
- Edit `blog/views.py` in VS Code:
  ```python
  from django.shortcuts import render

  def home(request):
      return render(request, 'blog/home.html')
  ```

---

## 10. Create Template
- Create folder structure: `blog/templates/blog/`.
- Create `blog/templates/blog/home.html` in VS Code:
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

## 11. Migrate Database
- Run migrations:
  ```bash
  python3 manage.py migrate
  ```

---

## 12. Run Server
- Start the development server:
  ```bash
  python3 manage.py runserver
  ```
  Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 13. Optional Extras
- **Create a superuser:**
  ```bash
  python3 manage.py createsuperuser
  ```

- **Access admin panel:**
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

- **Stop server:**
  ```bash
  Ctrl + C
  ```

- **Commit changes to Git:**
  ```bash
  git add .
  git commit -m "Completed Django project setup with blog app"
  ```

---

## 14. Common Fixes
| Error | Cause | Fix |
|-------|--------|-----|
| `TemplateDoesNotExist` | Wrong folder structure | Ensure `blog/templates/blog/home.html` exists |
| `ModuleNotFoundError` | App not added in settings | Add `'blog'` to `INSTALLED_APPS` in `settings.py` |
| `NameError` | Variable undefined in view | Define variables in `views.py` before use |

---

## Notes
- Use VS Code’s built-in terminal (set to **zsh/bash**) for commands.
- Ensure `.venv` is active before running Django commands.
- Refer to Django documentation or use ChatGPT for troubleshooting.
- Commit to Git after major steps for version control.
