## GETTING STARTED

* `$ [pipenv install django~=3.1.7](https://pipenv-fork.readthedocs.io/en/latest/basics.html#specifying-versions-of-a-package)`
* `$ pipenv shell`
* `$ django-admin startproject conf .`
* `$ python manage.py runserver`

## HEROKU

[Heroku Deployment](./../student-resources/heroku-deployment-guide/README.md)

## UNAPPLIED MIGRATIONS

You have 18 unapplied migration(s)...

Django is complaining that we have not yet "migrated" or configured our initial database.
We'll go ahead and migrate the built-in apps.

* `$ python manage.py migrate`

A Django project contains one or more apps within it that work together to power the application.

## CREATE APP

* `$ python manage.py startapp todos`
* `admin.py` is a configuration file for the built-in Django Admin app
* `apps.py` is a configuration file for the app itself
* `migrations/` keeps track of any changes to our `models.py`
* `models.py` is where we define our database models which Django uses to architect our database tables
* `tests.py` is for our app-specific tests
* `views.py` is where we handle request and response logic

We have to explicitly tell our Django project about each app we create

* `todos.apps.TodosConfig` inside `settings.py` under `INSTALLED_APPS`

Django reads our apps top to bottom. We want core apps available first since it's likely our own apps we rely on their functionality - e.g. admin, auth

Best practice - always use the full app config name like `todos.apps.TodosConfig`.

## VIEWS AND URL CONFIGURATION

Views determine ***what*** content is displayed on a given page while the url configuration determines ***where*** that content is going.

URL configuration maps a user's request for a specific page to the appropriate view.

* `todos/views.py`
```
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')
```
* touch `todos/urls.py`
* `todos/urls.py`
```
from django.urls import path


from .views import homePageView


app_name = 'todos'


urlpatterns = [
    path('', homePageView, name='home'),
]
```
* `conf/urls.py`
```
+ from django.urls import path, include
+ path('', include('todos.urls', namespace='todos')),
```
