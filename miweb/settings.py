import os
import json
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno
load_dotenv()

# Obtener BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Intentar obtener la configuración de Firebase desde las variables de entorno
FIREBASE_CRED = os.getenv("FIREBASE_CRED")

if FIREBASE_CRED:
    try:
        firebase_cred_dict = json.loads(FIREBASE_CRED)
        cred = credentials.Certificate(firebase_cred_dict)
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
    except json.JSONDecodeError:
        raise ValueError("⚠️ FIREBASE_CRED no contiene un JSON válido.")
else:
    raise ValueError("⚠️ No se encontró la credencial de Firebase en las variables de entorno.")

# 🔹 Seguridad: Cargar SECRET_KEY desde .env
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")

# 🔹 Modo Debug
DEBUG = os.getenv("DEBUG", "True") == "True"

# 🔹 Hosts permitidos
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost,miweb-hqp6.onrender.com").split(",")

# 🔹 Definición de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
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

ROOT_URLCONF = 'miweb.urls'

# 🔹 Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'principal', 'templates')],
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

WSGI_APPLICATION = 'miweb.wsgi.application'

# 🔹 Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔹 Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Configuración de localización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🔹 Archivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# 🔹 Configuración de la clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

