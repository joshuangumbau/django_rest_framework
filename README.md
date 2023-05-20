# django_rest_framework
django_rest_framework with restful api
To-do list to create a REST API in Django
    Set up Django
    Create a model in the database that the Django ORM will manage
    Set up the Django REST Framework
    Serialize the model from step 2
    Create the URI endpoints to view the serialized data
    
     Set up Django
     curl https://pyenv.run | bash  to install pyenv
     echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
     echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
     to reload bash source ~/.bashrc
     
pyenv virtualenv django-rest
pyenv local django-rest
pip install django to -install django 
django-admin startproject mysite to start a django project

cd mysite 

python manage.py runserver

python manage.py startapp myapi - to create a reactapi

Register the myapi app with the mysite project
We need to tell Django to recognize this new app that we just created. The steps we do later won’t work if Django doesn’t know about myapi.INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my.api.apps.MyapiConfig',
]
Create Super User
python manage.py createsuperuser

Create a model in the database that Django ORM will manage
# models.py
from django.db import modelsclass Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)  
    def __str__(self):
        return self.name
name and alias are character fields where we can store strings. The __str__ method just tells Django what to print when it needs to print out an instance of the Hero model.

//Make migrations
python manage.py makemigrations
python manage.py migrate

//Register the model Hero with the admin sitefrom django.contrib import admin
from .models import Hero
admin.site.register(Hero)

//Set up Django REST Framework
Okay, time to start thinking about our heroes API. We need to serialize the data from our database via endpoints.

To do that, we’ll need Django REST Framework, so let’s get that installed.
$ pip install djangorestframework
Now, tell Django that we installed the REST Framework in mysite/settings.py:

INSTALLED_APPS = [
    # All your installed apps stay the same
    ...
    'rest_framework',
]

//Serialize the Hero model
We need to tell REST Framework about our Hero model and how it should serialize the data.

Remember, serialization is the process of converting a Model to JSON. Using a serializer, we can specify what fields should be present in the JSON representation of the model.
The serializer will turn our heroes into a JSON representation so the API user can parse them, even if they’re not using Python. In turn, when a user POSTs JSON data to our API, the serializer will convert that JSON to a Hero model for us to save or validate.
To do so, let’s create a new file — myapi/serializers.py

//Display the data
Now, all that’s left to do is wire up the URLs and views to display the data!
Let’s start with the view. We need to render the different heroes in JSON format.

To do so, we need to:

    Query the database for all heroes
    Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered

In myapi/views.py:

// Site URLs



