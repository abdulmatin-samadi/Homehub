"""
HomeHub loyihasi uchun Django sozlamalari.

Bu loyiha O'zbekiston uchun ko'chmas mulk platformasi bo'lib,
bosqichma-bosqich rivojlantiriladi. Hozircha faqat 'users' app'i ulangan,
keyingi qadamlarda properties, favorites, reviews, chat, payments,
dashboard va api app'lari qo'shiladi.
"""

from pathlib import Path

# Loyiha ildiz papkasi
BASE_DIR = Path(__file__).resolve().parent.parent

# XAVFSIZLIK OGOHLANTIRISHI: production muhitida bu kalitni maxfiy saqlang
# va environment variable orqali yuklang (masalan os.environ orqali).
SECRET_KEY = 'django-insecure-CHANGE-THIS-KEY-IN-PRODUCTION-!!!'

# Production muhitida DEBUG = False qilib qo'ying
DEBUG = True

ALLOWED_HOSTS = ['*']  # Production'da aniq domenlarni ko'rsating


# ============ APPLICATION DEFINITION ============
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Uchinchi tomon
    'rest_framework',

    # HomeHub ilovalari
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'properties.apps.PropertiesConfig',
    'favorites.apps.FavoritesConfig',
    'reviews.apps.ReviewsConfig',
    'chat.apps.ChatConfig',
    'payments.apps.PaymentsConfig',
    'dashboard.apps.DashboardConfig',
    'api.apps.ApiConfig',
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

ROOT_URLCONF = 'homehub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Global shablonlar papkasi (barcha app'lar uchun umumiy)
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'homehub.wsgi.application'


# ============ DATABASE ============
# Dastlab SQLite ishlatiladi. PostgreSQL'ga o'tish uchun quyidagini
# almashtiring:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'homehub_db',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============ PASSWORD VALIDATION ============
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Custom foydalanuvchi modeli (users app ichida)
AUTH_USER_MODEL = 'users.User'

# Login/logout yo'naltirishlari
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'pages:home'
LOGOUT_REDIRECT_URL = 'pages:home'


# ============ INTERNATIONALIZATION ============
# Sayt faqat O'zbek tilida ishlaydi
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True


# ============ STATIC & MEDIA FILES ============
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Foydalanuvchi yuklaydigan fayllar (avatar, uy rasmlari va h.k.)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============ DJANGO REST FRAMEWORK ============
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
}
