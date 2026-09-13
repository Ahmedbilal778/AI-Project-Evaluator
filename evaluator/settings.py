from pathlib import Path
from dotenv import load_dotenv
import os


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Load local .env if available
load_dotenv(BASE_DIR / ".env")


# =========================================================
# SECURITY
# =========================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-dev-only-change-this-key"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
).lower() == "true"


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]


# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "evaluator_app",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# =========================================================
# URL CONFIG
# =========================================================

ROOT_URLCONF = "evaluator.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [

    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "evaluator.wsgi.application"


# =========================================================
# DATABASE
# =========================================================

DB_HOST = os.getenv("DB_HOST", "localhost")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",

        "NAME": os.getenv(
            "DB_NAME",
            "ai_project_evaluator"
        ),

        "USER": os.getenv(
            "DB_USER",
            "root"
        ),

        "PASSWORD": os.getenv(
            "DB_PASSWORD",
            ""
        ),

        "HOST": DB_HOST,

        "PORT": os.getenv(
            "DB_PORT",
            "3306"
        ),

        "CONN_MAX_AGE": 60,
    }
}

# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# =========================================================
# MEDIA FILES
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# CSRF
# =========================================================

CSRF_TRUSTED_ORIGINS = [

    "https://*.onrender.com",
]


# =========================================================
# EMAIL
# =========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)