from pathlib import Path
import os, sys


BASE_DIR = Path(__file__).resolve().parent.parent.parent
# set apps default directory
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'django-insecure-)(l24zm8w=6(^%4r7a0qa@jm8-@*$^7ed1z9d#8tjwhra)(gt8'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party
    'crispy_forms',
    'allauth',
    'allauth.account',

    # local apps
    'apps.authentication.apps.AuthenticationConfig',
    'apps.vendor.apps.VendorConfig',
    'apps.message.apps.MessageConfig',
    'apps.customer.apps.CustomerConfig',
    'apps.blog.apps.BlogConfig',
    'apps.forum.apps.ForumConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.vendor.context_processor.cart_items_counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
MEDIA_ROOT = "media/"

STATICFILES_DIRS = [
    BASE_DIR / "static/",
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
SITE_ID = 1

# Authentication
AUTH_USER_MODEL = "authentication.Account"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_VERIFICATION = "none"


ACCOUNT_FORMS = {
    'signup': 'apps.authentication.forms.RegisterForm'
}

LOGIN_REDIRECT_URL = 'customer:home'