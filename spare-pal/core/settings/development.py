from .base import *

# Login url
LOGIN_URL = 'http:/localhost:3000/auth/login'

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# CORS settings
# For demo purposes only. Use a white list in the real world.
CORS_ORIGIN_ALLOW_ALL = True