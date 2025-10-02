# Intro to Modern App dev - Lecture **3**

## Lecture summary:

1. Setting up a django project
2. The project HQ (settings.py & main urls.py)
3. Essential settings & configurations
4. Using .env files for secrets
5. MVT architecture, URLs, ORM
6. Setting up django apps
7. Designing URLs
8. Setting up templates & jinja
9. Models & Migrations


## Setting up a Django project (revisit from lecture 2)

Django is a python web framework.

### Steps to set up a new django project

1. Please follow all the steps from Using uv section. In dependencies, add "django" and run the sync command. Activate virtual env.
2. Delete `main.py`. We do not need this for django.
3. Run `django-admin startproject <project_name> .` This will set up the project in the same directory where uv project was set up. Again, PLEASE ENSURE CORRECT DIRECTORY.
4. This will create two artifacts: a python script `manage.py` and a python module with the provided project name. 
5. Once step 4 is complete, we can test the setup by running the in-built development server. Run
`uv run manage.py runserver`. This should launch a server on `127.0.0.1:8000`. You should see the following 


## The settings.py file

This is the main brain of the project, residing in the head project directory.
All essential settings inlcuding databases, templates, deployements, etc are managed here. 

Important settings:
* SECRET_KEY: A key used by django to hash and encrypt passwords
* DEBUG: Setting info level for logging
* INSTALLED_APPS: All associated apps in the project (default + user created)
* TEMPLATES: Specify directory path for template files
* STATIC_FILES: Specify path for static files

There are other several settings which we will explore as we go deeper into the setup

## Using .env file

This is the best way to manage credentials, keys and other sensitive data. Another important way of using environment variables is to configure settings. This practice lets you change settings without making changes to the code (for instance, you can set DEBUG through env)

PLEASE FOLLOW THIS PRACTICE WIHTOUT FAIL. **VERY CRUCIAL**

## MVT Architecture


![MVT Architecture](assets/mvt.png)

* Models: Data classes that become a table in the Database. An instance of this class is a row in the table
* Views: The core logic that connects Models with Templates
* ORM: Object-Relational Mapper that is a set of django in-built modules that help you interact with the database. This connects Views with Models.
* Templates: HTML files that display the information using Jinja, python's template engine
* URL: Uniform Resource Locator that maps templates with views. Users use URL to access specific templates

## Setting up Django apps

Django follows a monolithic architecture, which means it hosts all the backend and frontend code on a single server. So to handle separation of concern, django uses 'apps'. An app is a single module that consists of Models and Views related to one topic / concern.

### To create an app

`django-admin startapp <app_name>`

Once apps are create, in settings.py, add the name of the app to `INSTALLED_APPS`. This allows the Django HQ to recognize the app as a part of its system.


## Designing URLs

A Uniform Resource Locator (URL) creates a map to every view. A single URL maps to a single view that allows users to access them. URLs are managed at two levels in Django

1. `<main_project_directory>/urls.py` : Here we define urls that are at the "upper" level of the application. Each url in this file connects to a set of urls in specific apps. We use the `include()` function to map to app urls
2. `<app_directory/urls.py>`: Connect each path to a view

## Setting up Django Templates

Templates refer to the HTML files combined with Jinja. The templating engine allows for dynamic population of data. The engine allows using advanced capabilites that would not work with HTML files otherwise. Here are some tags that we used:

- {% load static %} - Loads all static files that allow using static file paths
- {% block name %}{% endblock name %} - Creating blocks of content to use in other files
- {% extends filename %} - Extend skeletal structure of base HTML files
- {% for element in elements %}{% endfor %} - For loop
- {% url 'url' %} - Using url names in anchor tag href
- {% static 'static_file_path' %} - paths to static files
- {{ data }} - populate data sent from a view

### Common practise

Extracting head, footer, nav and create a base or common html file. Extend this file into other files and use block tags

