#Learning Django

##Here are some basic django commands

###To srtart a django project - this will create a new project
django-admin startproject ProTwo

###To start a new application
python manage.py startapp appTwo

###Migrate databases
python manage.py migrate

####Make migration of actual application
python manage.py makemigrations appTwo

###Create Superuser
python manage.py createsuperuser
