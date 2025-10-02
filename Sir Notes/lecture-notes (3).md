# Intro to Modern App dev - Lecture **4**

The complete blog project implementation is available. Please go through it.

## Lecture Sumamry

1. Revisit to MVT, URL, ORM (see Lecture 3 notes)
2. Setting up migrations
3. Database designing - Connecting Models
4. Primary / Foreign Keys, using UUIDs
5. GET / POST requests
6. CSRF Tokens
7. render vs redirect

## Setting up migrations

Database designing in django / any backend system is performed incrementally. Each step of this design is called a 'Migration'.
A migration refers to the state of the models (current design of model classes) that are directly connected to the Database

Migrations are handled at app level. This means that you will find a `migrations/` directory in every app module. As more migrations
are made, the Django ORM will generate migration files incrementally.

## Database designing

As your django app increases in size and complexity, more and more Models will have to be defined across apps. Naturally, these tables
are going to be connected through some links.

These links are called **keys** (read more on DBMS)

### There are mainly two types of keys used in these tables

* Primary keys: Unique identifier for each row
* Foreign keys: A Field (typically primary keys) of another table which links the two tables

### There are two main ways of forming a relationship b/w two tables

* One to Many
* Many to Many

Models connected to other models through Foreign Keys typically need a fallback mechanism, in case an instance / row of the Main model
is deleted. Based on context, an `on_delete` parameter has to be set for each FK field

* CASCADE - if the main instance is deleted, all referered instances will be deleted. (Blog -> Blog Comment)
* SET_NULL - if the main instance is deleted, all referered instances are set to NULL. (Teacher -> Student)

### Using UUIDs for Primary Keys

Counter based integer IDs are simple to use. They are also what Django and several other frameworks use as default. But the simplicity comes with a trade-off.

These keys are normally used in URL parameters to request data. Any user can simply manipulate these URLs to try and access data which is off limits to them (typically you would have another layer of check before fetching this data, e.g, checking the authenticated user but this is a vulnerability still)

To address this, we use UUIDs (Universally Unique Identifiers). These are 36 characters long, randomly generated strings that are used as Primary Keys


## GET / POST requests

So far we have seen

* Requesting the server for some data (All blogs, specific blogs)
* Sending some data to the server (Posting comments)

While we don't formally define the type of requests a view takes, we do however associate a view with a type of request. In more advanced implementations, we will see how the same view can serve multiple types of requests.

The request parameter that is passed to every contains a key called `method`. You can check `request.method` to identify a request.


## CSRF Tokens

When making post requests, it is crucial to let the backend server know who is making the request. If request are accepted from unknown sources,
this can lead to security problems. Therefore, a CSRF token is included in every POST request we make.

From the Template HTML, we include the tag `{% csrf_token %}` every time a form is defined. This lets django know that a CSRF token must be included.
In later implementations, we will see how csrf checks can be bypassed.

## render() vs redirect()

We use the render function when we associate a view to a template. The render function takes the complete request, along with a specific template file
and some context data. This is essential for GET requests, where the user has explicitly requested for some data.

In case of other requests, POST, PUT, DELETE; we do not render a complete page, but often lead the user back to the same / another rendered page. This is where we use the `redirect()` function. It takes as arguement, only the url name (specified in paths of urls.py). This does not re-render a page, but simply redirects the user back to a rendered page.
