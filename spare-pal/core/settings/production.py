from .base import *

# Security
SECRET_KEY = config("SECRET_KEY")

# Debug
DEBUG = config("DEBUG", default=False, cast=bool)

# Allowed Hosts
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# CORS allowed origins
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "'smtp.mailgun.org'"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME", 'project_db'),
        "USER": config("USER", 'project_db_usr'),
        "PASSWORD": config("DB_PASSWORD", 'projet_db_pwd'),
        "HOST": config("DB_HOSTNAME", 'db'),
        "PORT": config("DB_PORT", cast=int),
    }
}

# Caching(No need of caching in development)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": config("REDIS_BACKEND"),
    },
}

# LOGIN_URL = 'http:/sparepal.com/auth/login'
