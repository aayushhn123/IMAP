Django Project Setup Cheat Sheet (Windows)
This cheat sheet guides you through setting up a Django project on Windows using VS Code, based on Lecture Notes 1-4 from "Intro to Modern App Dev." It uses Git Bash for Unix-like commands (recommended for consistency with Git and uv), Python 3.12+, and uv for package management. Covers virtual environments, Git, .env, apps, URLs, templates, and migrations.
Prerequisites

Install Python from python.org (avoid Anaconda to prevent conflicts).
Install Git (includes Git Bash) from git-scm.com.
Use Git Bash as your terminal for Linux-like commands (ls, source).
Familiarize with commands: cd (change dir), dir (list files), mkdir (make dir).
Open VS Code: code . from project root in Git Bash.


1. Install uv (Rust-Based Package Manager)
uv is a modern Python package manager (Lecture 2).

Preferred Method (PowerShell):
irm https://astral.sh/uv/install.ps1 | iex


Alternative (if PowerShell fails, use CMD/Git Bash):
pip install uv


Verify:
uv --version

If not recognized, restart Git Bash or add uv to PATH (troubleshoot with ChatGPT).

Note: If Python issues arise (e.g., from Anaconda), reinstall native Python.



2. Create Project Directory and Initialize uv Project

Create a root directory:
mkdir my-projects
cd my-projects


Initialize uv project:
uv init my-django-project  # Replace with your project name
cd my-django-project


Open in VS Code:
code .


Files Created:

pyproject.toml: Dependencies and config.
.python-version: Locks Python version.
README.md: Document your project.
.gitignore: Edit later.




3. Add Dependencies and Sync

Edit pyproject.toml in VS Code:
[project]
name = "my-django-project"
version = "0.1.0"
dependencies = ["django", "python-dotenv"]  # For .env


Sync dependencies:
uv sync

Creates .venv/ and installs Django.

Activate Virtual Environment (Git Bash):
source .venv/Scripts/activate

Alternative (CMD/PowerShell):
.venv\Scripts\activate

Verify: Prompt shows (.venv). Deactivate with deactivate.

Delete unneeded file:
del main.py




4. Initialize Git (Version Control)
From Lecture 1: Track changes early.

Initialize Git repo:
git init


Edit .gitignore in VS Code:
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


Stage and commit:
git add .
git commit -m "Initial project setup with uv and Git"


Check Status/History:
git status
git log --oneline


Later (GitHub): Create repo on GitHub, then:
git remote add origin <url>
git push -u origin main




5. Start Django Project
From Lectures 2 & 3: Sets up core Django files.

Run in project root (venv active; check dir with dir):
django-admin startproject core .


Artifacts Created:

manage.py: CLI for Django commands.
core/ directory: Contains settings.py, urls.py, etc.


Test setup:
uv run manage.py runserver

Visit http://127.0.0.1:8000/ to see Django welcome page.



6. Configure Essential Settings (settings.py)
From Lecture 3: Edit core/settings.py.

Key Settings:

SECRET_KEY: Move to .env.
DEBUG = True: For dev.
INSTALLED_APPS: Add custom apps later.
TEMPLATES: Add 'DIRS': [BASE_DIR / 'templates'].
STATIC_URL = 'static/': Add STATICFILES_DIRS = [BASE_DIR / 'static'].


Use .env for Secrets:

Ensure "python-dotenv" in pyproject.toml; run uv sync.
Create .env (add to .gitignore):SECRET_KEY=your-secret-key-here
DEBUG=True


Update settings.py:from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'






7. Set Up Django Apps, URLs, Templates, and MVT Basics
From Lecture 3: Django uses MVT (Models-Views-Templates).

Create an App:
django-admin startapp blog


Add to INSTALLED_APPS in settings.py:INSTALLED_APPS = [
    ...,
    'blog',
]




Design URLs:

Main: Edit core/urls.py:from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]


App: Create blog/urls.py:from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
]




Set Up Templates:

Create templates/ in project root or app.
In templates/base.html:{% load static %}
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


Extend in other templates: {% extends 'base.html' %}.
Tags: {% for %}, {% url 'name' %}, {{ variable }}, {% csrf_token %}.


Static Files: Create static/; use {% static 'path' %}.



8. Database Setup and Migrations
From Lectures 3 & 4: Uses ORM.

Default DB: SQLite (settings.py: DATABASES).

Create Models in blog/models.py.

Migrations:
uv run manage.py makemigrations
uv run manage.py migrate


Advanced (Lecture 4):

UUID Primary Keys:import uuid
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


ForeignKey: Use on_delete=models.CASCADE or SET_NULL.
Run migrations after model changes.




9. Views, Requests, and Rendering
From Lecture 4.

In blog/views.py:
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        # Handle POST
        return redirect('blog-home')
    return render(request, 'blog/home.html', {'context': data})


CSRF for POST: Add {% csrf_token %} in forms.



10. Common Commands and Tips

Run server: uv run manage.py runserver
Create superuser: uv run manage.py createsuperuser
Collect static: uv run manage.py collectstatic
Check directory: dir
Deactivate venv: deactivate
Troubleshooting: Use ChatGPT for errors; ensure correct dir and venv.
MVT: Models (DB), Views (Logic), Templates (UI); URLs map views; ORM connects DB.
Commit to Git after major steps.
Refer to Lecture 4 for blog project example.
