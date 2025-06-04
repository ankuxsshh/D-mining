from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-74yo+mom$eb^sj(wx8$5zx09$i1m5^ycj+v4+3c_z9+bshc#hg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "DMININGapp",  
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "DMININGproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Custom templates directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DMININGproject.wsgi.application"

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_app_password'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONTACT_RECEIVER_EMAIL = 'your_website_email@example.com'


# settings.py

################################################################################
# JAZZMIN SETTINGS
################################################################################

JAZZMIN_SETTINGS = {
    # ---------------------------
    # Site Branding
    # ---------------------------
    "site_title": "D-Mining Admin",
    "site_header": "D-Mining Dashboard",
    "site_brand": "D-Mining",
    # (You can use an icon file placed in STATIC_ROOT/jazzmin/img/... if you like)
    # "site_logo": "jazzmin/img/jazzmin-logo.png",

    # ---------------------------
    # Top Navigation Links
    # ---------------------------
    "topmenu_links": [
        {"name": "Home", "url": "/", "permissions": []},
        {"model": "auth.User"},  # Links directly to built-in User model
    ],

    # ---------------------------
    # User Menu Settings
    # ---------------------------
    "usermenu_links": [
        {"name": "My Profile", "url": "/admin/auth/user/your-user-id/change/", "icon": "fas fa-user"},
        {"model": "auth.Group", "icon": "fas fa-users"},
    ],

    # ---------------------------
    # UI Tweaks (Colors, Fonts, etc.)
    # ---------------------------
    "theme": "cosmo",          # Bootswatch theme: cerulean, cosmo, slate, etc.
    "dark_mode_theme": "cyborg",
    "welcome_sign": "Welcome to D-Mining Admin",
    "copyright": "D-Mining © 2025",
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": [
        "auth",                # All auth app models get grouped first
        "DMININGapp.ContactInfo",
        "DMININGapp.CourseModal",
        "DMININGapp.Carousel",
        # You can list other models here in any order you prefer
    ],

    # ---------------------------
    # Model Icons (FontAwesome) and Custom Ordering
    # ---------------------------
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "DMININGapp.ContactInfo": "fas fa-address-book",
        "DMININGapp.CourseModal": "fas fa-graduation-cap",
        "DMININGapp.Carousel": "fas fa-images",
    },

    # ---------------------------
    # Remove Apps/Models you don’t want to show:
    # ---------------------------
    "hide_apps": [],
    "hide_models": [],

    # ---------------------------
    # Search Placeholders
    # ---------------------------
    "search_model": "DMININGapp.ContactInfo",
}

# You can also add JAZZMIN_UI_TWEAKS if you want finer control over colors/fonts:
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "sidebar_nav_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,

    "accent": "accent-primary",   # Bootswatch accent color class
    "navbar": "bg-primary",
    "footer": "footer-dark",      # “footer-dark” or “footer-light”
    "sidebar": "sidebar-dark",    # “sidebar-dark” or “sidebar-light”
    "sidebar_nav_color": "sidebar-nav-light",
    "sidebar_bg": "sidebar-bg-primary",
    "sidebar_brand_color": "sidebar-brand-light",
}
