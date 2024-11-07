Dependencies
------------

#. Bulma - 0.9.3

#. Font Awesome - 6.0.0

#. Python - 3.12.0

#. Django - 5.0.3

#. MongoDB - 1.44.6

# Django Certificate Form Application
Tutorial for building create, retrieve, update and delete CRUD application with Django using MongoDB(Using MongoDB Compass)

### Prerequisites

Make sure you have installed Python 3 and virtual environment on your device.

1. Install django and start new project inside your directory according the above structure
```
django-admin startproject login
cd login
```
2. Create new app, from login/ directory will create create new my_app/ to store the collection
```
On Windows -> python manage.py startapp my_app
```
3. Every after change models.py you need to make migrations into MongoDB (database) to create the table for the new model
```
python manage.py makemigrations
python manage.py migrate
```
4. Test the project
```
python manage.py runserver
```
