# Django Projects Setup (Windows, VS Code)

This file contains **both Ekart/E-commerce and Blog project setups** for Django on Windows using VS Code.

---

## 1️⃣ Ekart/E-commerce Project Setup

### Main terminal
```powershell
cd <your-directory>
uv init
cd <project-folder>
code .
```

### pyproject.toml
```toml
dependencies = [
    "django",
    "python-dotenv"
]
```

### VS Code Terminal
*Run one by one*
```powershell
uv venv --python=3.10.6
.venv\Scripts\activate
uv sync
```

*Delete main.py*

```powershell
django-admin startproject <projectname> .   # eg - ekart
```

### Project setting.py
```python
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
```
*create .env folder outside of ekart*

### .env
```env
SECRET_KEY="django-insecure-dm+k7&!b_*2^imgvplos5_6(1fd-&%xh@y(d(l@dn-%-=$1%rz"
DEBUG="1"
```

### In setting.py
```python
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True if os.getenv("DEBUG") == "1" else False
```

### VS Code Terminal
```powershell
mkdir templates static
```

### In setting.py
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,"templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR,"static"),)
```

*Drop the html files in templates and assets in static*

### VS Code Terminal
```powershell
django-admin startapp <appname>   # eg users
```

### In setting.py
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
]
```

### urls.py (in ekart)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('users.urls'))
]
```

### users -> create urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index')
]
```

### users -> views.py
Optional:
```python
from django.shortcuts import render , HttpResponse

def index(request):
    return HttpResponse('<h1>Hello from ekart<h1>')
```

### VS Code Terminal
```powershell
uv run manage.py runserver
```

### Actual views.py
```python
from django.shortcuts import render , HttpResponse

def index(request):
    return render(request , 'index.html')
```

### templates -> create common folder -> create base folder
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    {% block title %}{% endblock title %}
    <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i">
</head>
<body style="background:linear-gradient(rgba(47, 23, 15, 0.65), rgba(47, 23, 15, 0.65)), url('static/img/bg.jpg');">
{% block body %}{% endblock body %}
<footer class="footer text-faded text-center py-5">
    <div class="container">
        <p class="m-0 small">Copyright&nbsp;©&nbsp;Brand 2021</p>
    </div>
</footer>
<script src="{% static 'assets/js/jquery.min.js' %}"></script>
<script src="{% static 'assets/bootstrap/js/bootstrap.min.js' %}"></script>
<script src="{% static 'assets/js/current-day.js' %}"></script>
</body>
</html>
```

### templates -> index.html
```html
{% extends 'common/base.html' %}
{% block title %}
<title>Index</title>
{% endblock title %}

{% block body %}
{% load static %}
<section class="page-section clearfix">
    <div class="container">
        <div class="intro"><img class="img-fluid intro-img mb-3 mb-lg-0 rounded" src="/static/img/intro.jpg">
            <div class="intro-text left-0 text-centerfaded p-5 rounded bg-faded text-center">
                <h2 class="section-heading mb-4"><span class="section-heading-upper">Fresh Coffee</span><span class="section-heading-lower">Worth Drinking</span></h2>
                <p class="mb-3">Every cup of our quality artisan coffee starts with locally sourced, hand picked ingredients...</p>
                <div class="mx-auto intro-button"><a class="btn btn-primary d-inline-block mx-auto btn-xl" role="button" href="#">Visit Us Today!</a></div>
            </div>
        </div>
    </div>
</section>
{% endblock body %}
```

### Models.py
```python
from django.db import models

class blog(models.Model):
    blog_title=models.CharField(max_length=600)
    blog_content=models.TextField(max_length=1000)
```

### Admin.py
```python
from django.contrib import admin
from .models import blog

admin.site.register(blog)
```

### Commands
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Views.py
```python
from django.shortcuts import render,HttpResponse
from .models import blog

def index(request):
    data=blog.objects.all()
    return render(request,"index.html",{"abc":data})
```

### Urls.py
```python
from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index")
]
```

### GIT
```powershell
git init
git remote add origin https://github.com/<user name>/<repo name>.git
git add .
git commit -m "Initial commit: Ekart project"
git branch -M main
git push -u origin main
```

---

## 2️⃣ Blog Project Setup

### Base.html
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    {% block title %}{% endblock title %}
    <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic">
    <link rel="stylesheet" href="{% static 'fonts/font-awesome.min.css' %}">
</head>
<body>
    <nav class="navbar navbar-light navbar-expand-lg fixed-top" id="mainNav">
        <div class="container"><a class="navbar-brand" href="index.html">Brand</a>
        <button data-toggle="collapse" data-target="#navbarResponsive" class="navbar-toggler" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><i class="fa fa-bars"></i></button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="nav navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="about.html">About us</a></li>
                <li class="nav-item"><a class="nav-link" href="contact.html">Contact us</a></li>
                <li class="nav-item"><a class="nav-link" href="post.html">Blog Post</a></li>
            </ul>
        </div>
        </div>
    </nav>
    <header class="masthead" style="background-image:url({% static 'img/home-bg.jpg' %});">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-md-10 col-lg-8 mx-auto">
                    <div class="site-heading">
                        <h1>Clean Blog</h1><span class="subheading">A Blog Theme by Start Bootstrap</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
    {% block body %}{% endblock body %}
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-md-10 col-lg-8 mx-auto">
                    <ul class="list-inline text-center">
                        <li class="list-inline-item"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-twitter fa-stack-1x fa-inverse"></i></span></li>
                        <li class="list-inline-item"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-facebook fa-stack-1x fa-inverse"></i></span></li>
                        <li class="list-inline-item"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-github fa-stack-1x fa-inverse"></i></span></li>
                    </ul>
                    <p class="text-muted copyright">Copyright&nbsp;©&nbsp;Brand 2021</p>
                </div>
            </div>
        </div>
    </footer>
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/clean-blog.js' %}"></script>
</body>
</

