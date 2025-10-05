# Django Contact Book Web Application Setup (Mac, VS Code)

This guide provides detailed steps, commands, and code to build a two-page contact book web application using Django on a Mac with VS Code and the default Terminal. The main page displays a list of contacts in clickable cards (showing name and contact number), and clicking a contact navigates to a detail page showing all information: name, contact number, email, organization, and creation timestamp. The guide is adapted from a Windows-based Django cheat sheet, modified for Mac, using Python 3.12+, `venv`, and SQLite (default database).

## Prerequisites
- **Python 3.12+**: Install from [python.org](https://python.org) (avoid Anaconda to prevent conflicts).
- **Git**: Install from [git-scm.com](https://git-scm.com) or via Homebrew (`brew install git`).
- **VS Code**: Install from [code.visualstudio.com](https://code.visualstudio.com).
- **Terminal**: Use macOS Terminal (default) for commands (`ls`, `source`).
- **Basic Commands**: Familiarize with `cd` (change directory), `ls` (list files), `mkdir` (make directory).
- **Open VS Code**: Run `code .` from project root in Terminal (ensure VS Code command-line tools are installed: in VS Code, press `Cmd+Shift+P`, select "Shell Command: Install 'code' command in PATH").

## 1. Create Project Directory
Create and navigate to the project directory:
```bash
mkdir contactbook
cd contactbook
```

Open in VS Code:
```bash
code .
```

## 2. Create & Activate Virtual Environment
Create a virtual environment:
```bash
python3 -m venv .venv
```

Activate it in Terminal:
```bash
source .venv/bin/activate
```

Verify: Prompt shows `(.venv)`. Deactivate with `deactivate`.

## 3. Install Django
With the virtual environment active, install Django:
```bash
pip install django
```

## 4. Initialize Git (Optional but Recommended)
Initialize a Git repository:
```bash
git init
```

Create a `.gitignore` file in VS Code:
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

Stage and commit:
```bash
git add .
git commit -m "Initial project setup with venv and Git"
```

## 5. Start Django Project
Run in the project root (venv active; check directory with `ls`):
```bash
django-admin startproject core .
```

**Artifacts Created:**
- `manage.py`: CLI for Django commands.
- `core/` directory: Contains `settings.py`, `urls.py`, etc.

Test the setup:
```bash
python3 manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the Django welcome page. Stop with `Ctrl+C`.

## 6. Create the Contacts App
Create a Django app:
```bash
python3 manage.py startapp contacts
```

**Folder Structure:**
```
contactbook/
├── .venv/
├── manage.py
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── contacts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
```

## 7. Define the Contact Model
Edit `contacts/models.py` in VS Code:
```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

- `CharField`: For name, contact number, organization.
- `EmailField`: Validates email format.
- `DateTimeField` with `auto_now_add=True`: Sets timestamp on creation.
- `__str__`: Returns name for admin/list display.

## 8. Add App to Settings
Edit `core/settings.py`:

Add `'contacts'` to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contacts',  # Add this
]
```

Verify template settings:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # Enables app-level templates
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

## 9. Make Migrations and Migrate
Create migration files:
```bash
python3 manage.py makemigrations
```

Apply migrations to create database tables (uses SQLite):
```bash
python3 manage.py migrate
```

## 10. Set Up Admin for Adding Contacts (Optional for Testing)
Register the model in admin for easy data entry.

Edit `contacts/admin.py`:
```python
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
```

Create a superuser:
```bash
python3 manage.py createsuperuser
```

Follow prompts for username, email, password. Access admin at `http://127.0.0.1:8000/admin/` after starting the server.

## 11. Create Views
Edit `contacts/views.py`:
```python
from django.shortcuts import render, get_object_or_404
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all().order_by('-creation_timestamp')  # Newest first
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})
```

- `contact_list`: Fetches all contacts, sorted by newest first.
- `contact_detail`: Fetches a contact by primary key (pk), or 404 if not found.
- Uses Django’s ORM for database queries.

## 12. Set Up URLs
Create `contacts/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('<int:pk>/', views.contact_detail, name='contact_detail'),
]
```

Edit `core/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),  # Root URL for contacts app
]
```

- Root (`''`) maps to the contact list.
- `<int:pk>/` maps to detail view (e.g., `/1/` for contact with pk=1).

## 13. Create Templates
Create folder: `contacts/templates/contacts/`.

### Main Page (Contact List with Cards)
Create `contacts/templates/contacts/contact_list.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact Book</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .card { border: 1px solid #ccc; padding: 10px; margin: 10px; width: 300px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
        .card a { text-decoration: none; color: black; }
        .card:hover { background-color: #f9f9f9; }
    </style>
</head>
<body>
    <h1>Contact Book</h1>
    <div style="display: flex; flex-wrap: wrap;">
        {% for contact in contacts %}
            <div class="card">
                <a href="{% url 'contact_detail' contact.pk %}">
                    <h2>{{ contact.name }}</h2>
                    <p>Contact Number: {{ contact.contact_number }}</p>
                </a>
            </div>
        {% empty %}
            <p>No contacts available.</p>
        {% endfor %}
    </div>
</body>
</html>
```

- Displays contacts as clickable cards (name, number).
- Uses flexbox for layout.
- Jinja `{% url %}` for linking to details.

### Detail Page
Create `contacts/templates/contacts/contact_detail.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ contact.name }} - Details</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .detail { border: 1px solid #ccc; padding: 20px; max-width: 600px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>{{ contact.name }} - Contact Details</h1>
    <div class="detail">
        <p><strong>Name:</strong> {{ contact.name }}</p>
        <p><strong>Contact Number:</strong> {{ contact.contact_number }}</p>
        <p><strong>Email:</strong> {{ contact.email }}</p>
        <p><strong>Organization:</strong> {{ contact.organization }}</p>
        <p><strong>Creation Timestamp:</strong> {{ contact.creation_timestamp }}</p>
    </div>
    <a href="{% url 'contact_list' %}">Back to Contact List</a>
</body>
</html>
```

- Shows all contact fields.
- Includes a back link to the list.

## 14. Run Server and Test
Start the server:
```bash
python3 manage.py runserver
```

- Visit `http://127.0.0.1:8000/` for the contact list.
- Add contacts via admin (`http://127.0.0.1:8000/admin/`), e.g., 2-3 entries.
- Click a card to view details (e.g., `http://127.0.0.1:8000/1/`).
- Stop server with `Ctrl+C`.

## 15. Commit Changes to Git (Optional)
```bash
git add .
git commit -m "Implemented contact book app with list and detail views"
```

## 16. Common Fixes
| Error | Cause | Fix |
|-------|-------|-----|
| `TemplateDoesNotExist` | Wrong template path | Ensure `contacts/templates/contacts/` contains `contact_list.html` and `contact_detail.html`. |
| `NoReverseMatch` | Incorrect URL name | Verify `name='contact_list'` and `name='contact_detail'` in `urls.py`. |
| `ModuleNotFoundError` | App not in settings | Add `'contacts'` to `INSTALLED_APPS` in `settings.py`. |
| Empty list | No data | Add contacts via admin panel. |

## Notes
- **Testing**: Use admin to add contacts (e.g., Name: John Doe, Contact Number: +1234567890, Email: john@example.com, Organization: Acme Corp).
- **Styling**: Basic CSS used; for better design, add Bootstrap CDN in `<head>`: `<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">` and use classes like `card`, `container`.
- **Security**: For production, use UUIDs for primary keys (`id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)` in `models.py`) to prevent URL guessing.
- **Database**: SQLite is used (default); for production, configure PostgreSQL in `settings.py`.
- **Extensions**: Add forms for creating/editing contacts via POST requests (requires `CSRF_TOKEN` as per Theory.md).
- **MVT Architecture**: Model (Contact), Views (list/detail), Templates (HTML with Jinja).
- Refer to Django docs or ask for help with errors.

This completes a functional two-page contact book web app with a card-based list and detailed view, adhering to the requirements, tailored for macOS.
