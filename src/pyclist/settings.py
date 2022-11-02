"""
Django settings for pyclist project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import tempfile
import warnings
from os import path

import pycountry
from django.core.paginator import UnorderedObjectListWarning
from django.utils.translation import gettext_lazy as _
from environ import Env
from stringcolor import cs

from pyclist import conf

# disable UnorderedObjectListWarning when using autocomplete_fields
warnings.filterwarnings('ignore', category=UnorderedObjectListWarning)

# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

env = Env()
env.read_env(env('DJANGO_ENV_FILE'))
env.read_env(env('DJANGO_DB_CONF', default='/run/secrets/db_conf'))

ADMINS = conf.ADMINS

MANAGERS = ADMINS

EMAIL_HOST = conf.EMAIL_HOST
EMAIL_HOST_USER = conf.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = conf.EMAIL_HOST_PASSWORD
EMAIL_PORT = conf.EMAIL_PORT
EMAIL_USE_TLS = conf.EMAIL_USE_TLS

SERVER_EMAIL = 'Clist <%s>' % EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = 'Clist <%s>' % EMAIL_HOST_USER

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = conf.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = env('DJANGO_ENV') == 'dev'

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'clist',
    'ranking',
    'tastypie',
    'my_oauth',
    'true_coders',
    'jsonify',  # https://pypi.python.org/pypi/django-jsonify/0.2.1
    'tastypie_swagger',
    'tg',
    'notification',
    'crispy_forms',
    'events',
    'django_countries',
    'el_pagination',
    'django_static_fontawesome',
    'django_extensions',
    'django_user_agents',
    'django_json_widget',
    'django_ltree',
    'imagefit',
    'webpush',
    'django_postgres_reindex_command',
    'oauth2_provider',
    'tastypie_oauth',
    'channels',
    'chats',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'pyclist.middleware.SetUpCSRFToken',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'csp.middleware.CSPMiddleware',
    'pyclist.middleware.UpdateCoderLastActivity',
    'pyclist.middleware.RequestLoggerMiddleware',
    'pyclist.middleware.RedirectMiddleware',
    'pyclist.middleware.SetAsCoder',
    'pyclist.middleware.Lightrope',
)

if DEBUG:
    DEBUG_PERMISSION_EXCLUDE_PATHS = {'static', 'imagefit'}
    MIDDLEWARE += (
        'pyclist.middleware.DebugPermissionOnlyMiddleware',
        'django_cprofile_middleware.middleware.ProfilerMiddleware',
    )
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ROOT_URLCONF = 'pyclist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pyclist.context_processors.global_settings',
                'pyclist.context_processors.bootstrap_admin',
                'pyclist.context_processors.coder_time_info',
                'pyclist.context_processors.fullscreen',
            ],
            'builtins': [
                'pyclist.templatetags.staticfiles',
                'clist.templatetags.extras',
                'imagefit.templatetags.imagefit',
                'django.contrib.humanize.templatetags.humanize',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyclist.wsgi.application'

ASGI_APPLICATION = 'pyclist.asgi.application'
if DEBUG:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        }
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {'hosts': [('0.0.0.0', 'redis')]},
        },
    }


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES_ = {
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    },
}

DATABASES = {
    'default': DATABASES_['postgresql'],
}
DATABASES.update(DATABASES_)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
        'OPTIONS': {
            'server_max_value_length': 1024 * 1024 * 10,
        },
    }
}

USER_AGENTS_CACHE = 'default'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [path.join(BASE_DIR, 'static')]
REPO_STATIC_ROOT = path.join(BASE_DIR, 'static/')
STATIC_JSON_TIMEZONES = path.join(BASE_DIR, 'static', 'json', 'timezones.json')

STATICFILES_STORAGE = 'static_compress.CompressedStaticFilesStorage'
STATIC_COMPRESS_METHODS = ['gz']


MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'mediafiles')

TASTYPIE_DEFAULT_FORMATS = ['json', 'jsonp', 'yaml', 'xml', 'plist']

LOGIN_URL = '/login/'

APPEND_SLASH = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'db': {
            'format': str(cs('[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s', 'grey')),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'console-debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'console-info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'db': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'db',
        },
        'development': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': path.join(BASE_DIR, 'logs', 'dev.log'),
            'formatter': 'verbose',
        },
        'production': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': path.join(BASE_DIR, 'logs', 'prod.log'),
            'formatter': 'verbose',
        },
        'telegrambot': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': path.join(BASE_DIR, 'logs', 'telegram.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'PIL': {
            'handlers': ['null'],
            'propagate': False,
        },
        'googleapiclient.discovery': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
        },
        'telegrambot': {
            'handlers': ['telegrambot'],
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['db'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console-debug', 'console-info', 'development', 'production'],
            'level': 'INFO',
        },
    },
}


DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000


TELEGRAM_TOKEN = conf.TELEGRAM_TOKEN
TELEGRAM_NAME = conf.TELEGRAM_NAME
TELEGRAM_ADMIN_CHAT_ID = conf.TELEGRAM_ADMIN_CHAT_ID

CRISPY_TEMPLATE_PACK = 'bootstrap3'

COUNTRIES_OVERRIDE = {
    'CZ': {'names': ['Czech Republic', 'Czechia', 'Чехия']},
    'MK': {'names': ['Macedonia', 'North Macedonia', 'Македония']},
    'PS': {'names': ['Palestine', 'Palestine, State of', 'Палестина']},
    'KR': {'names': ['South Korea', 'Republic of Korea', 'Южная Корея', 'Korea, Republic of']},
    'MO': {'names': ['Macao', 'Macau', 'Макао']},
    'US': {'names': ['United States of America', 'United States', 'America', 'Virgin Islands', 'UM', 'United States Minor Outlying Islands', 'Соединенные Штаты Америки', 'США']},  # noqa
    'VN': {'names': ['Vietnam', 'Viet Nam', 'Вьетнам']},
    'GB': {'names': ['United Kingdom', 'United Kingdom of Great Britain', 'England', 'UK', 'Scotland', 'Northern Ireland', 'Wales', 'Великобритания', 'Англия', 'Шотландия']},  # noqa
    'MD': {'names': ['Moldova', 'Молдова', 'Молдавия', 'Republic of Moldova', 'Moldova, Republic of']},
    'KG': {'names': ['Kyrgyzstan', 'Кыргызстан', 'Киргизия']},
    'RS': {'names': ['Serbia', 'Srbija', 'Сербия']},
    'HR': {'names': ['Croatia', 'Hrvatska', 'Хорватия']},
    'CN': {'names': ['China', '中国', 'Китай']},
    'PL': {'names': ['Poland', 'Republic of Poland', 'Польша']},
    'RU': {'names': ['Russia', 'Россия', 'Russian Federation', 'Российская Федерация']},
    'SU': {'names': ['Soviet Union', 'Советский Союз']},
}
DISABLED_COUNTRIES = {'UM'}


ALPHA2_FIXES_MAPPING = {
    'AIDJ': 'A0',
    'BQAQ': 'B0',
    'BYAA': 'B1',
    'GEHH': 'G0',
    'SKIN': 'S0',
    'CSXX': 'Y0',
}

for country in pycountry.historic_countries:
    code = ALPHA2_FIXES_MAPPING.pop(country.alpha_4, country.alpha_2)
    assert not pycountry.countries.get(alpha_2=code)

    override = COUNTRIES_OVERRIDE.setdefault(code, {})
    assert not override.get('alpha3')
    names = [name.strip() for name in country.name.split(',')]
    assert names
    if names[-1].endswith(' of'):
        assert len(names) > 1
        names[-1] += ' ' + names[0]
    names = [name for name in names if not pycountry.countries.get(name=name)]

    override.setdefault('names', []).extend(names)
    if not pycountry.countries.get(alpha_3=country.alpha_3):
        override.setdefault('alpha3', country.alpha_3)
    if hasattr(country, 'numeric'):
        override.setdefault('numeric', country.numeric)


CUSTOM_COUNTRIES_ = {
    'BY': ['BY', 'BPR'],
}

# DJANGO DEBUG TOOLBAR
if DEBUG:
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_PANELS = [
      'debug_toolbar.panels.history.HistoryPanel',
      'debug_toolbar.panels.versions.VersionsPanel',
      'debug_toolbar.panels.timer.TimerPanel',
      'debug_toolbar.panels.settings.SettingsPanel',
      'debug_toolbar.panels.headers.HeadersPanel',
      'debug_toolbar.panels.request.RequestPanel',
      'debug_toolbar.panels.sql.SQLPanel',
      'debug_toolbar.panels.staticfiles.StaticFilesPanel',
      'debug_toolbar.panels.templates.TemplatesPanel',
      'debug_toolbar.panels.cache.CachePanel',
      'debug_toolbar.panels.signals.SignalsPanel',
      'debug_toolbar.panels.logging.LoggingPanel',
      'debug_toolbar.panels.redirects.RedirectsPanel',
      'debug_toolbar.panels.profiling.ProfilingPanel',
    ]

    def show_toolbar_callback(request):
        first_path = request.path.split('/')[1]
        return (
            first_path not in DEBUG_PERMISSION_EXCLUDE_PATHS and
            not request.is_ajax() and
            'disable_djtb' not in request.GET and
            (not DEBUG or request.user.is_authenticated)
        )

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar_callback,
        'DISABLE_PANELS': {
            'debug_toolbar.panels.templates.TemplatesPanel',
            'debug_toolbar.panels.redirects.RedirectsPanel',
            'debug_toolbar.panels.request.RequestPanel',
        },
    }

# DJANGO CPROFILE
DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False

# DGANGO IMAGEFIT
IMAGEFIT_CACHE_ENABLED = True
IMAGEFIT_CACHE_BACKEND_NAME = 'django_imagefit'
CACHES[IMAGEFIT_CACHE_BACKEND_NAME] = {
    'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    'LOCATION': path.join(tempfile.gettempdir(), 'django_imagefit' + ('_debug' if DEBUG else ''))
}

# BOOSTRAP ADMIN
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

# WEBPUSH
WEBPUSH_SETTINGS = conf.WEBPUSH_SETTINGS

# OAUTH2 PROVIDER
OAUTH2_PROVIDER = {
    'DEFAULT_SCOPES': ['read'],
}


CSRF_COOKIE_SECURE = True

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Content Security Policy
CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", "https:", "data:")
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'")
CSP_IMG_SRC = CSP_DEFAULT_SRC
CSP_CONNECT_SRC = CSP_DEFAULT_SRC

# CSP Yandex counter
CSP_SCRIPT_SRC += ('https://mc.yandex.ru', 'https://yastatic.net', )
CSP_IMG_SRC += ('https://mc.yandex.ru', )
CSP_CONNECT_SRC += ('https://mc.yandex.ru', )

# CSP Google counter
CSP_SCRIPT_SRC += ('https://www.google-analytics.com', 'https://www.googletagmanager.com', )
CSP_IMG_SRC += ('https://www.google-analytics.com', )
CSP_CONNECT_SRC += ('https://www.google-analytics.com', )

# X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

# CONSTANTS
VIEWMODE_ = 'list'
OPEN_NEW_TAB_ = False
ADD_TO_CALENDAR_ = 'enable'
COUNT_PAST_ = 3
GROUP_LIST_ = True
HIDE_CONTEST_ = False
DEFAULT_TIME_ZONE_ = 'UTC'
HOST_ = 'dev.clist.by' if DEBUG else 'clist.by'
HTTPS_HOST_ = 'https://' + HOST_
MAIN_HOST_ = 'https://clist.by'
CLIST_RESOURCE_DICT_ = {
    'host': HOST_,
    'pk': 0,
    'icon': 'img/favicon/favicon-32x32.png',
    'kind': 'global_rating',
    'colors': [],
}
EMAIL_PREFIX_SUBJECT_ = '[Clist] '
STOP_EMAIL_ = getattr(conf, 'STOP_EMAIL', False)
TIME_FORMAT_ = '%d.%m %a %H:%M'
LIMIT_N_TOKENS_VIEW = 3
LIMIT_TOKENS_VIEW_WAIT_IN_HOURS = 24
YES_ = {'', '1', 'yes', 'y', 'true', 't', 'on'}
ACE_CALENDARS_ = {
    'enable': {'id': 'enable', 'name': 'Enable'},
    'disable': {'id': 'disable', 'name': 'Disable'},
    'google': {'id': 1, 'name': 'Google'},
    'yahoo': {'id': 2, 'name': 'Yahoo'},
    'outlook': {'id': 3, 'name': 'Outlook'},
}
PAST_CALENDAR_ACTIONS_ = ['show', 'lighten', 'darken', 'lighten-day', 'darken-day', 'hide']
PAST_CALENDAR_DEFAULT_ACTION_ = 'lighten'
ORDERED_MEDALS_ = ['gold', 'silver', 'bronze']
THEMES_ = ['default', 'cerulean', 'cosmo', 'cyborg', 'darkly', 'flatly', 'journal', 'lumen', 'paper', 'readable',
           'sandstone', 'simplex', 'slate', 'spacelab', 'superhero', 'united', 'yeti']

DEFAULT_COUNT_QUERY_ = 10
DEFAULT_COUNT_LIMIT_ = 100

ISSUES_URL_ = 'https://github.com/aropan/clist/issues'
NEWS_URL_ = 'https://t.me/s/clistbynews'
DISCUSS_URL_ = 'https://t.me/clistbynews'
DONATE_URL_ = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=47CJBL6B2XPM8&source=url'

ADDITION_HIDE_FIELDS_ = {'problems', 'solved'}

VIRTUAL_CODER_PREFIX_ = '∨'

DEFAULT_API_THROTTLE_AT_ = 10

CODER_LIST_N_VALUES_LIMIT_ = 100

ENABLE_GLOBAL_RATING_ = DEBUG

FONTAWESOME_ICONS_ = {
    'institution': '<i class="fa-fw fas fa-university"></i>',
    'country': '<i class="fab fa-font-awesome-flag"></i>',
    'room': '<i class="fa-fw fas fa-door-open"></i>',
    'affiliation': '<i class="fa-fw fas fa-user-friends"></i>',
    'city': '<i class="fa-fw fas fa-city"></i>',
    'school': '<i class="fa-fw fas fa-school"></i>',
    'class': '<i class="fa-fw fas fa-user-graduate"></i>',
    'job': '<i class="fa-fw fas fa-building"></i>',
    'rating': '<i class="fa-fw fas fa-chart-line"></i>',
    'medal': '<i class="fa-fw fas fa-medal"></i>',
    'region': '<i class="fa-fw fas fa-map-signs"></i>',
    'chat': '<i class="fa-fw fas fa-user-friends"></i>',
    'advanced': '<i class="fa-fw far fa-check-circle"></i>',
    'company': '<i class="fa-fw fas fa-building"></i>',
    'language': '<i class="fa-fw fas fa-code"></i>',
    'languages': '<i class="fa-fw fas fa-code"></i>',
    'league': '<i class="fa-fw fas fa-chess"></i>',
    'degree': '<i class="fa-fw fas fa-user-graduate"></i>',
    'university': '<i class="fa-fw fas fa-university"></i>',
    'list': '<i class="fa-fw fas fa-list"></i>',
    'group': '<i class="fa-fw fas fa-user-friends"></i>',
    'group_ex': '<i class="fa-fw fas fa-user-friends"></i>',
    'college': '<i class="fa-fw fas fa-university"></i>',
    'resource': '<i class="fa-fw fas fa-at"></i>',
    'field': '<i class="fa-fw fas fa-database"></i>',
    'find_me': '<i class="fa-fw fas fa-crosshairs"></i>',
    'search': '<i class="fa-fw fas fa-search"></i>',
    'detail_info': '<i class="fa-fw fas fa-info"></i>',
    'short_info': '<i class="fa-fw fas fa-times"></i>',
    'score_in_row': '<i class="fa-fw fas fa-balance-scale"></i>',
    'luck': '<i class="fa-fw fas fa-dice"></i>',
    'tag': '<i class="fa-fw fas fa-tag"></i>',
    'hide': '<i class="fa-fw far fa-eye-slash"></i>',
    'show': '<i class="fa-fw far fa-eye"></i>',
    'period': '<i class="fa-fw far fa-clock"></i>',
    'date': '<i class="fa-fw far fa-calendar-alt"></i>',
    'n_participations': {'icon': '<i class="fa-fw fas fa-running"></i>', 'title': 'Number of participations'},
    'chart': '<i class="fa-fw fas fa-chart-bar"></i>',
    'ghost': '<i class="fs-fw fas fa-ghost"></i>',
    'top': {'icon': '<i class="fas fa-list-ol"></i>', 'title': 'Top for resource'},
    'versus': '<i class="fas fa-people-arrows"></i>',
    'last_activity': '<i class="fa-fw far fa-clock"></i>',
    'fullscreen': '<i class="fas fa-expand-arrows-alt"></i>',
    'charts': '<i class="fas fa-chart-bar"></i>',
    'update': '<i class="fas fa-sync"></i>',

    'google': {'icon': '<i class="fab fa-google"></i>', 'title': None},
    'facebook': {'icon': '<i class="fab fa-facebook"></i>', 'title': None},
    'youtube': {'icon': '<i class="fab fa-youtube"></i>', 'title': None},
    'twitch': {'icon': '<i class="fab fa-twitch"></i>', 'title': None},
    'github': {'icon': '<i class="fab fa-github"></i>', 'title': None},
    'yandex': {'icon': '<i class="fab fa-yandex-international"></i>', 'title': None},
    'discord': {'icon': '<i class="fab fa-discord"></i>', 'title': None},
    'vk': {'icon': '<i class="fab fa-vk"></i>', 'title': None},
    'patreon': {'icon': '<i class="fab fa-patreon"></i>', 'title': None},
}


class NOTIFICATION_CONF:
    EMAIL = 'email'
    TELEGRAM = 'telegram'
    WEBBROWSER = 'webbrowser'

    METHODS_CHOICES = (
        (EMAIL, 'Email'),
        (TELEGRAM, 'Telegram'),
        (WEBBROWSER, 'WebBrowser'),
    )


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
