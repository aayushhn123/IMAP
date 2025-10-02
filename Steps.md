# Django Project Setup Cheat Sheet

This cheat sheet provides a step-by-step guide to setting up a Django project, based on Lecture Notes 1-4 from "Intro to Modern App Dev." It assumes you're using **VS Code**, Python 3.12+, and a Unix-like terminal (e.g., Git Bash on Windows; adjust for PowerShell/CMD if needed). Covers uv package management, virtual environments, Git, .env, apps, URLs, templates, and migrations.

## Prerequisites
- Install **Python** from [python.org](https://python.org) (avoid Anaconda to prevent conflicts).
- Install **Git** from [git-scm.com](https://git-scm.com).
- Familiarize with terminal commands: `cd` (change directory), `ls`/`dir` (list files), `mkdir` (make directory).
- Open VS Code: Use `code .` from project root in terminal.

---

## 1. Install uv (Rust-Based Package Manager)
uv is a modern Python package manager (Lecture 2).

- **Preferred Method (PowerShell on Windows or Terminal on Mac/Linux):**
  ```bash
  irm https://astral.sh/uv/install.ps1 | iex  # Windows PowerShell
  ```
  OR
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh  # Mac/Linux
  ```

- **Alternative (if PowerShell fails):**
  ```bash
  pip install uv
  ```

- **Verify:**
  ```bash
  uv --version
  ```
  If not recognized, restart terminal or add uv to PATH (troubleshoot with ChatGPT).

- **Tip (Windows):** Use Git Bash for uv, Git, and Linux commands in one terminal. If Python issues (e.g., from Anaconda), reinstall native Python.

---

## 2. Create Project Directory and Initialize uv Project
- Create a root directory for projects:
  ```bash
  mkdir my-projects
  cd my-projects
  ```

- Initialize uv project:
  ```bash
  uv init my-django-project  # Replace with your project name
  cd my-django-project
  ```

- Open in VS Code:
  ```bash
  code .
  ```

- **Files Created:**
  - `pyproject.toml`: Dependencies and config.
  - `.python-version`: Locks Python version (no edits needed).
  - `README.md`: Document your project.
  - `.gitignore`: For Git; edit later.

---

## 3. Add Dependencies and Sync
- Edit `pyproject.toml` in VS Code to add Django:
  ```toml
  [project]
  name = "my-django-project"
  version = "0.1.0"
  dependencies = ["django", "python-dotenv"]  # Add python-dotenv for .env
  ```

- Sync dependencies (installs packages in virtual env):
  ```bash
  uv sync
  ```
  Creates `.venv/` and installs Django.

- **Activate Virtual Environment:**
  - Mac/Linux/Git Bash:
    ```bash
    source .venv/bin/activate
    ```
  - Windows (PowerShell/CMD):
    ```bash
    .venv\Scripts\activate
    ```
  Verify: Prompt shows `(.venv)`. Deactivate with `deactivate`.

- Delete unneeded file (Lecture 2):
  ```bash
  rm main.py  # Or del main.py on Windows
  ```

---

## 4. Initialize Git (Version Control)
From Lecture 1: Track changes early.

- Initialize Git repo:
  ```bash
  git init
  ```

- Edit `.gitignore` in VS Code (add sensitive files; Lectures 1 & 3):
  ```gitignore
  # Python/Django specifics
  *.pyc
  *.pyo
  __pycache__/
  .venv/
  db.sqlite3  # Default dev DB
  .env  # For secrets

  # Logs and temp
  *.log
  *.pot
  *.mo
  ```

- Stage and commit:
  ```bash
  git add .
  git commit -m "Initial project setup with uv and Git"
  ```

- **Check Status/History:**
  ```bash
  git status  # View changes
  git log --oneline  # Commit history
  ```

- **Later (GitHub):** Create repo on GitHub, then:
  ```bash
  git remote add origin <url>
  git push -u origin main
  ```

---

## 5. Start Django Project
From Lectures 2 & 3: Sets up core Django files.

- Run in project root (ensure venv active; check dir with `ls`/`dir`):
  ```bash
  django-admin startproject core .  # 'core' is common; '.' sets up in current dir
  ```

- **Artifacts Created:**
  - `manage.py`: CLI for Django commands.
  - `core/` directory: Contains `settings.py`, `urls.py`, etc. (project "HQ").

- Test setup:
  ```bash
  uv run manage.py runserver
  ```
  Visit `http://127.0.0.1:8000/`. Should see Django welcome page (rocket ship).

---

## 6. Configure Essential Settings (settings.py)
From Lecture 3: Edit `core/settings.py`.

- **Key Settings:**
  - `SECRET_KEY`: Move to .env.
  - `DEBUG = True`: For dev (set via .env).
  - `INSTALLED_APPS`: Add custom apps later.
  - `TEMPLATES`: Add `'DIRS': [BASE_DIR / 'templates']` for project-wide templates.
  - `STATIC_URL = 'static/'`: Add `STATICFILES_DIRS = [BASE_DIR / 'static']`.

- **Use .env for Secrets (Lecture 3, Crucial):**
  - Ensure `"python-dotenv"` in `pyproject.toml`; run `uv sync`.
  - Create `.env` in root (add to `.gitignore`):
    ```env
    SECRET_KEY=your-secret-key-here  # Copy from settings.py
    DEBUG=True
    ```
  - Update `settings.py`:
    ```python
    from pathlib import Path
    import os
    from dotenv import load_dotenv

    load_dotenv()  # At top

    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG') == 'True'
    ```

---

## 7. Set Up Django Apps, URLs, Templates, and MVT Basics
From Lecture 3: Django uses MVT (Models-Views-Templates).

- **Create an App:**
  ```bash
  django-admin startapp blog  # Example app
  ```
  - Add to `INSTALLED_APPS` in `settings.py`:
    ```python
    INSTALLED_APPS = [
        ...,
        'blog',
    ]
    ```

- **Design URLs:**
  - Main: Edit `core/urls.py`:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls')),  # Links to app URLs
    ]
    ```
  - App: Create `blog/urls.py`:
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='blog-home'),
    ]
    ```

- **Set Up Templates (Jinja-Enabled HTML):**
  - Create `templates/` in project root or app.
  - In `templates/base.html`:
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}My Site{% endblock %}</title>
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
        {% block content %}{% endblock %}
    </body>
    </html>
    ```
  - Extend in other templates: `{% extends 'base.html' %}`.
  - Common Tags: `{% for %}`, `{% url 'name' %}`, `{{ variable }}`, `{% csrf_token %}` (for POST forms).

- **Static Files:** Create `static/` dir; use `{% static 'path' %}` in templates.

---

## 8. Database Setup and Migrations
From Lectures 3 & 4: Uses ORM for DB interaction.

- **Default DB:** SQLite (`settings.py`: `DATABASES`).
- Create Models in `blog/models.py` (e.g., `Blog(models.Model)`).
- **Migrations:**
  ```bash
  uv run manage.py makemigrations  # Create migration files
  uv run manage.py migrate  # Apply to DB
  ```

- **Advanced (Lecture 4):**
  - UUID Primary Keys:
    ```python
    import uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ```
  - ForeignKey: Use `on_delete=models.CASCADE` or `SET_NULL`.
  - Run migrations after model changes.

---

## 9. Views, Requests, and Rendering
From Lecture 4.

- In `blog/views.py`:
  ```python
  from django.shortcuts import render, redirect

  def home(request):
      if request.method == 'POST':
          # Handle POST
          return redirect('blog-home')
      return render(request, 'blog/home.html', {'context': data})  # GET: Render
  ```

- **CSRF for POST:** Add `{% csrf_token %}` in HTML forms.

---

## 10. Common Commands and Tips
- Run server: `uv run manage.py runserver`
- Create superuser: `uv run manage.py createsuperuser` (for admin)
- Collect static: `uv run manage.py collectstatic`
- Check directory: `ls`/`dir`
- Deactivate venv: `deactivate`
- **Troubleshooting:** Use ChatGPT/Gemini for errors; ensure correct dir and venv.
- **MVT Reminder:** Models (DB), Views (Logic), Templates (UI); URLs map views; ORM connects DB.
- Commit to Git after major steps.
- Refer to Lecture 4 for full blog project example.
