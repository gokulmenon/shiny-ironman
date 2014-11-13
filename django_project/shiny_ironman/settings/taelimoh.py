########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASE_OPTIONS = {"charset":"uft8"}

# Running in development, so use a local MySQL database.
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'USERNAME',
            'PASSWORD': 'PASSWORD',
            'HOST': 'localhost',
            'NAME': 'DBNAME',
    }
}
########## END DATABASE CONFIGURATION