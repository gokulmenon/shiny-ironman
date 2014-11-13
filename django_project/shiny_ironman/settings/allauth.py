########## ALL AUTH CONFIGURATION
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'SCOPE': ['email', 'publish_stream', 'publish_actions', 'photo_upload'],
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False},
    'google':
        { 'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile','email'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True

ACCOUNT_AUTHENTICATION_METHOD="username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET=True
ACCOUNT_UNIQUE_EMAIL=True
ACCOUNT_EMAIL_VERIFICATION="mandatory"
ACCOUNT_FORMS={'signup' : 'custom_user.forms.RegistrationForm'}
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_LOGOUT_ON_GET=True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION=False
ACCOUNT_SESSION_REMEMBER=True
ACCOUNT_USERNAME_BLACKLIST = ['_ah','404','500','admin','about','privacy','terms','contact','accounts','post','group',
                          'follow', 'api','society', 'search']
########## END ALL AUTH CONFIGURATION