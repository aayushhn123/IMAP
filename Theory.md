# Modern Application Development: Theory Notes for MCQs

These notes cover theoretical concepts from Lectures 1–4, designed for quick review to prepare for multiple-choice questions (MCQs). The content is organized by lecture and topic, focusing on definitions, key ideas, and relationships relevant for testing.

## Lecture 1: Introduction, HTML, CSS, and Git

### Introduction to Modern App Development
- The course focuses on building web applications using modern tools, frameworks, and version control systems.

### Git: Version Control System
- **Definition**: Git is a version control system for tracking code changes; GitHub is a platform for remote code storage and collaboration.
- **Key Concepts**:
  - A repository stores project history.
  - Commits are snapshots with unique IDs, author details, and timestamps.
  - `.gitignore` prevents sensitive data (e.g., API keys, `.env` files) from being tracked.
  - Advanced features include branches (parallel development), pull requests (code review), and merge conflicts (issues during code integration).

### HTML: Web Structure
- **Definition**: HTML (HyperText Markup Language) is a markup language for structuring web content.
- **Key Elements**:
  - `<head>`: Contains metadata, styles, and scripts.
  - Structural tags: `<div>` (container), `<h1>`–`<h6>` (headings), `<p>` (paragraphs), `<a>` (links), `<img>` (images).
  - Tables: `<table>`, `<tr>` (rows), `<th>` (headers), `<td>` (data cells).
  - Lists: `<ol>` (ordered), `<ul>` (unordered), `<li>` (list items).
  - Forms: `<form>` for user input.
  - `<style>` and `<script>` embed CSS and JavaScript.
  - Attributes: `id` (unique identifier), `class` (group styling).

### CSS: Web Styling
- **Definition**: CSS (Cascading Style Sheets) controls the visual presentation of HTML elements.
- **Key Concepts**:
  - Styling methods: Inline (within tags), internal (`<style>` tag), external (separate files).
  - Selectors target elements by tag, class, or ID.
  - Cascading rules prioritize styles based on specificity and order.

## Lecture 2: Backend Engineering, Python, and Django Basics

### Backend Engineering Concepts
- **Server**: A machine with hardware (CPU, RAM, storage) and an IP address, processing client requests.
- **Client-Server Cycle**: Clients request data; servers process and respond.
- **HTTP**:
  - **Status Codes**:
    - Success: 200 (OK), 201 (Created), 204 (No Content).
    - Client Errors: 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 422 (Unprocessable Entity).
    - Server Errors: 500 (Internal Server Error).
  - **REST Request Types**:
    - GET: Retrieve data.
    - POST: Submit data.
    - PUT: Update entire data.
    - PATCH: Update partial data.
    - DELETE: Remove data.
- **API**: Rules for data interaction over networks.
- **REST API**: Uses JSON for standardized data exchange.
- **Server-Side Rendering (SSR)**: Server generates and sends fully rendered HTML to clients.
- **Idempotency**: Operations (e.g., GET) producing consistent results regardless of repetition.

### Python Language Specifications
- **Characteristics**:
  - Synchronous: Executes sequentially.
  - Single-Threaded: Runs one thread by default.
  - High-Level: Abstracts complex operations.
  - Scripting Language: Suited for automation.
  - Dynamically Typed: Types determined at runtime.
  - Interpreted: Executes without compilation.

### UV: Python Project Management
- **Purpose**: Rust-based tool for managing Python projects.
- **Key Files**:
  - `pyproject.toml`: Configures dependencies and settings.
  - `.python-version`: Specifies Python version.
  - `uv.lock`: Locks dependencies for consistency.
  - `README.md`: Documents project details.
  - `.gitignore`: Excludes files from Git.

### Django: Web Framework Basics
- **Definition**: Django is a Python framework for rapid web development.
- **Structure**:
  - `manage.py`: Core script for project tasks.
  - Project module: Contains configuration files.
- Development server runs on localhost for testing.

## Lecture 3: Django Core Concepts

### Django Configuration
- **settings.py**: Central configuration file managing:
  - `SECRET_KEY`: Encrypts sensitive data (e.g., passwords).
  - `DEBUG`: Controls logging/error visibility.
  - `INSTALLED_APPS`: Lists default and custom apps.
  - `TEMPLATES`: Sets template directory paths.
  - `STATIC_FILES`: Defines paths for static assets (CSS, images).
- **.env Files**: Store sensitive data (e.g., keys, credentials) and allow dynamic configuration without code changes.

### MVT Architecture
- **Definition**: Model-View-Template (MVT) is Django’s pattern for web development.
- **Components**:
  - **Models**: Classes mapping to database tables (instances are rows).
  - **Views**: Logic connecting models and templates.
  - **Templates**: HTML files with Jinja for dynamic content.
  - **ORM**: Django’s tool for database interaction, abstracting SQL.
  - **URLs**: Map requests to views/templates.
- Django uses a monolithic architecture, with backend and frontend on one server, modularized via apps.

### Django Apps
- **Definition**: Modular units for specific concerns, containing related models and views.
- Must be registered in `INSTALLED_APPS` for integration.

### URL Design
- **Structure**:
  - Project-level `urls.py`: Defines high-level routes, linking to app URLs via `include()`.
  - App-level `urls.py`: Maps specific paths to views.

### Templates with Jinja
- **Definition**: HTML files using Jinja for dynamic rendering.
- **Key Features**:
  - Dynamic data population.
  - Common practice: Use a base template for shared elements (e.g., header, footer) with inheritance via `extends` and `block` tags.

## Lecture 4: Advanced Django Concepts

### Migrations
- **Definition**: Incremental changes to database schema based on model updates.
- Managed at the app level, stored in `migrations/` directories.
- ORM generates migration files to track schema evolution.

### Database Design
- **Model Relationships**:
  - One-to-Many: One instance links to multiple others.
  - Many-to-Many: Bidirectional connections between instances.
- **Keys**:
  - Primary Keys: Unique row identifiers (default: integers).
  - Foreign Keys: Link tables by referencing another table’s primary key.
- **On-Delete Behaviors**:
  - CASCADE: Deletes related instances if the primary is removed.
  - SET_NULL: Sets foreign keys to NULL on deletion.

### UUIDs for Primary Keys
- **Purpose**: 36-character random strings used as primary keys to prevent URL manipulation vulnerabilities, unlike predictable integer IDs.

### GET and POST Requests
- **GET**: Retrieves data (e.g., fetching blogs).
- **POST**: Submits data (e.g., posting comments).
- Views can handle multiple request types, identified via `request.method`.

### CSRF Tokens
- **Purpose**: Ensure POST requests originate from trusted sources, preventing cross-site request forgery.
- Included in forms to verify authenticity.

### render() vs redirect()
- **render()**: Associates views with templates, passing data for GET requests.
- **redirect()**: Sends users to another URL without re-rendering, used for POST, PUT, DELETE requests.

## Notes for MCQ Preparation
- **Focus Areas**:
  - Definitions (e.g., Git, HTML, CSS, Django, MVT, ORM).
  - Key components and their roles (e.g., settings.py, models, views, templates).
  - HTTP status codes and REST request types.
  - Python characteristics (e.g., synchronous, dynamically typed).
  - Database concepts (keys, relationships, migrations, UUIDs).
  - Security practices (CSRF tokens, .env files, UUIDs).
  - Differences (e.g., render vs redirect, primary vs foreign keys).
- **Tips**:
  - Memorize specific terms (e.g., CASCADE, SET_NULL, idempotency).
  - Understand relationships (e.g., MVT components, client-server cycle).
  - Review status codes and their categories (success, client, server).
