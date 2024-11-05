from .base import *

# Login url
LOGIN_URL = 'https://localhost:8000/users/login'

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# CORS settings
# For demo purposes only. Use a white list in the real world.
CORS_ORIGIN_ALLOW_ALL = True