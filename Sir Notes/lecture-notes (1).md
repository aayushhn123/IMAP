# Intro to Modern App dev - Lecture **2**

## Lecture summary:

1. Backend Engineering 101
2. Python theory - language specifications
3. Installing and using **uv**
4. Working with `pyproject.toml` files for managing python projects
5. Setting up a new django project
6. Anatomy of a django project
7. Launching a development server


## Backend Engineering concepts

* **Server** - Any machine with hardware resources (CPU, RAM, storage) and an IP address. Is accessible through the internet and performs some operations.
* **Client-Server Cycle** - Client - machine making requests / requesting and displaying information
* **HTTP Requests** - Types of requests, status codes, REST
* **API** - Application Programming Interface, defines a set of rules for interaction of data over web networks
* **REST API** - Representational State Transfer API / Use a standardized form of data exchange (JSON)
* **Server Side Rendering (SSR**) - Old School way of developing websites. Using HTML template engines (Jinja)

<br>

![Server Side Rendering](assets/ssr.png)

### HTTP

#### Request Status codes

* Success codes
> * 200 - OK
> * 201 - Created
> * 204 - No Content

* Client Side codes
> * 400 - Bad request
> * 401 - Unauthorized
> * 403 - Forbidden
> * 404 - Not Found
> * 422 - Unprocessable Entity

* Server side codes
> * 500 - Internal Server Error


#### Types of REST Requests

* GET - Request information
* POST - Submitting data
* PUT - Updating data
* PATCH - Updating part of the data
* DELETE - Delete some data

Extra read up -
* Idempotency - https://medium.com/@reetesh043/rest-api-design-what-is-idempotency-18218e1ff73c
* Documentation - Swagger OpenAPI (will be covered later) - https://swagger.io/resources/open-api/


## Basic Python specs

We explored the specifications / characteristics of Python

* Synchronous
* Single Threaded
* High level
* Scripting language
* Dynamically typed
* Interpreted

**TASK** Please use ChatGPT / Gemini to learn more about each of these paradigms. Very interesting stuff.

Get comfortable with this website - https://realpython.com/
This teaches you a lot about what is Python and how it is / should be used

## uv - The modern rust based package manager

### Installation steps

https://docs.astral.sh/uv/getting-started/installation/

On this page, you can find two ways to install uv on windows
1. Using Powershell - preferred
2. Using pip (if powershell does not work)

If uv is stil unrecognised after succesful installation, restart powershell / cmd. 

**TASK** Try to run uv from GitBash since then you can run linux commands, git, uv all from the same setup.

If there are issues with python on your system, use ChatGPT. There is literally no simpler way.  \
NOTE - if you previously used anaconda / miniconda, chances are native python is not available. Please proceed with a fresh installation of Python.

### Using uv

1. In a directory where you create all your projects, open gitbash / cmd / powershell. Run `uv init <project_name>`. This will create a new folder with the provided project name.
2. Open VS code directly from the newly created project folder.
3. This is the root directory of your project. You can find some basic setup files here.
> * pyproject.toml - Project config & dependencies (python packages)
> * .python-version - specifies python version for the project. No need to change / move this.
> * uv.lock - A frozen set of dependencies of your project. Created after sync
> * README.md - Have fun here. Write about your project.
> * .gitignore - Generated for git

4. After dependencies are specified in pyproject.toml, run `uv sync`. This will create a virtual env and install all the packages.
5. Proceed with activation of the virtual env
> * Mac / Linux - run `source .venv/bin/activate`
> * Windows - run `.venv\Scripts\activate`

Tip - Please PLEASE ensure that you are in the correct directory in terminal. Use `ls` (linux/mac) / `dir` (windows). This will show contents of the current directory.

## Setting up a Django project

Django is a python web framework.

### Steps to set up a new django project

1. Please follow all the steps from Using uv section. In dependencies, add "django" and run the sync command. Activate virtual env.
2. Delete `main.py`. We do not need this for django.
3. Run `django-admin startproject <project_name> .` This will set up the project in the same directory where uv project was set up. Again, PLEASE ENSURE CORRECT DIRECTORY.
4. This will create two artifacts: a python script `manage.py` and a python module with the provided project name. 
5. Once step 4 is complete, we can test the setup by running the in-built development server. Run
`uv run manage.py runserver`. This should launch a server on `127.0.0.1:8000`. You should see the following 

<br>

![Django Launch screen](assets/django.png)

**Congratulations!** You're ready for the next step.


We will be covering the directory structures and django python files in the next lecture. Will include details of those in next lecture notes.












