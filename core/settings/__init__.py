import os

from dotenv import load_dotenv

from core.settings.allowed_hosts import ALLOWED_HOSTS
from core.settings.auth_password_validators import AUTH_PASSWORD_VALIDATORS
from core.settings.databases import DATABASES
from core.settings.debug import DEBUG
from core.settings.default_auto_field import DEFAULT_AUTO_FIELD
from core.settings.django_settings_module import DJANGO_SETTINGS_MODULE
from core.settings.installed_apps import INSTALLED_APPS
from core.settings.language_code import LANGUAGE_CODE
from core.settings.middleware import MIDDLEWARE
from core.settings.rest_framework import REST_FRAMEWORK
from core.settings.root_urlconf import ROOT_URLCONF
from core.settings.static_url import STATIC_URL
from core.settings.templates import TEMPLATES
from core.settings.time_zone import TIME_ZONE
from core.settings.use_i18n import USE_I18N
from core.settings.user_tz import USE_TZ
from core.settings.wsgi_application import WSGI_APPLICATION

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
VAR_1 = os.getenv("VAR_1")
VAR_2 = os.getenv("VAR_2")
VAR_3 = os.getenv("VAR_3")
