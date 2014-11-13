=========================
sample-gae-django-project
=========================

A sample project for Django 1.5 used in Google Cloud Platform
(Google App Engine, Google Cloud SQL, and Google Cloud Storage).
This project also includes simple front-end development and design.

The site let's clients to post projects for freelancers.
Freelancers can apply to the projects,
and post portfolio to attract potential customers.

To use this project follow these steps:

#. Set Google Cloud Platform development environment
#. Install dependencies

Demo
====

http://dodme.com/

Project Structure
=================

shiny-ironman
-------------

Repository root. Includes django project, documentation, and requirements.

django_project
--------------

Django project root

* shiny_ironman : configuration root

docs
----

Documentation

requirements
------------

Requirement description files


Installation of Dependencies
=============================

Since you need to upload your dependencies to GAE along with your project,
you need to install them to the project folder. **requirements.sh** in
the project root directory will install requirments to **libs** directory.
Create symlinks from **libs** directory to the project directory
in order to upload your libraries with your GAE project.

Depending on where you are installing dependencies::

    $ ./requirements.sh


*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Google Cloud Platform
=====================

You need Google Cloud SQL and Google Cloud Storage to run Django code as-is on Google App Engine.

Google Cloud SQL
----------------

Refer to the link below and connect Google Cloud SQL to your project.

https://developers.google.com/appengine/docs/python/cloud-sql/django

Google Cloud Storage
--------------------

Refer to the link below and connect Google Cloud Storage to your project.

https://developers.google.com/storage

Fix **gae.py**, **local.py**, and **producttion.py** under **gluwa_job/settings** folder.

Acknowledgements
================

- Two Scoops: https://django.2scoops.org/
- Django-nonrel: http://django-nonrel.org/
- JetBrains: http://www.jetbrains.com/
- Designmodo: http://www.designmodo.com/