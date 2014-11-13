#!/usr/bin/env python
import os

# Load production settings when running on GAE or SETTINGS_MODE is prod
# else, load local settings
if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or os.getenv('SETTINGS_MODE') == 'prod'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shiny_ironman.settings.production")
    from production import *

    RUNNING_ON_APPENGINE = True
else:
    from local import *
    from taelimoh import *

    RUNNING_ON_APPENGINE = False


########## STORAGE CONFIGURATION
# See: https://github.com/ckopanos/django-google-cloud-storage
DEFAULT_FILE_STORAGE = 'gae.storage.googleCloud.GoogleCloudStorage'

GOOGLE_CLOUD_STORAGE_BUCKET = '/BUCKETNAME' # the name of the bucket you have created from the google cloud storage console
GOOGLE_CLOUD_STORAGE_URL = 'http://storage.googleapis.com/bucket' #whatever the url for accessing your cloud storgage bucket
GOOGLE_CLOUD_STORAGE_DEFAULT_CACHE_CONTROL = 'public, max-age: 7200' # default cache control headers for your files
########## END STORAGE CONFIGURATION

########## DATABASE CONFIGURATION
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'INSTANCE': 'INSTANCENAME:DBNAME',
            'NAME': 'DBNAME',
            'USER': 'USERNAME',
        }
    }
elif os.getenv('SETTINGS_MODE') == 'prod':
    # Running in development, but want to access the Google Cloud SQL instance
    # in production.
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'INSTANCENAME:DBNAME',
            'NAME': 'DBNAME',
            'USER': 'USERNAME',
        }
    }

########## END DATABASE CONFIGURATION