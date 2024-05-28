import logging
import os
from datetime import timedelta

from celery.schedules import crontab
from flask_caching.backends.rediscache import RedisCache

logger = logging.getLogger()

DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = (
    f"{DATABASE_DIALECT}://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_SSL_PORT = os.getenv("REDIS_SSL_PORT", 6380)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
REDIS_PASSWORD = REDIS_PASSWORD_PARAM = os.getenv("REDIS_PASSWORD", "")

if REDIS_PASSWORD_PARAM:
    REDIS_PASSWORD_PARAM = ":{}@".format(REDIS_PASSWORD_PARAM)

CACHE_DEFAULT_TIMEOUT = int(timedelta(hours=2).total_seconds()) # 2 hours

SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=30).total_seconds()) #30 minutes

REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

# Optionally, we might configure the SQL Lab cache as a file system cache
# RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST,
    port=REDIS_SSL_PORT,
    db=REDIS_RESULTS_DB,
    default_timeout=CACHE_DEFAULT_TIMEOUT,
    password=REDIS_PASSWORD,
    key_prefix='superset_results_',
    ssl=True
)

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": CACHE_DEFAULT_TIMEOUT,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
    "CACHE_REDIS_URL": f"redis://{REDIS_PASSWORD_PARAM}{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
}
DATA_CACHE_CONFIG = CACHE_CONFIG

class CeleryConfig:
    broker_url = f"redis://{REDIS_PASSWORD_PARAM}{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    imports = ("superset.sql_lab",)
    result_backend = f"redis://{REDIS_PASSWORD_PARAM}{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    worker_prefetch_multiplier = 1
    task_acks_late = False
    beat_schedule = {
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=10, hour=0),
        },
    }


CELERY_CONFIG = CeleryConfig

# Enable feature flags:
# - alerts and reports
# - template processing
# - tags
# - experimental chart plugins
# - alert reports
# - horizontal filter bar
# - use analagous colors
# - allow adhoc subquery
FEATURE_FLAGS = {"ALERT_REPORTS": True,
                 "ENABLE_TEMPLATE_PROCESSING": True,
                 "ALLOW_FULL_CSV_EXPORT": True,
                 "TAGGING_SYSTEM": True,
                 "CHART_PLUGINS_EXPERIMENTAL": True,
                 "ALERT_REPORTS": True,
                 "HORIZONTAL_FILTER_BAR": True,
                 "DASHBOARD_RBAC": True,
                 "ALLOW_ADHOC_SUBQUERY": True}
ALERT_REPORTS_NOTIFICATION_DRY_RUN = True
WEBDRIVER_BASEURL = os.getenv("WEBDRIVER_BASEURL", "http://superset:8088/")
# The base URL for the email report hyperlinks.
WEBDRIVER_BASEURL_USER_FRIENDLY = WEBDRIVER_BASEURL

SQLLAB_CTAS_NO_LIMIT = True

# Disabling Python stack traces by default
SHOW_STACKTRACE = os.environ.get("SHOW_STACKTRACE", False)

# Cache configuration
REDIS_CACHE_DB = os.environ.get("REDIS_CACHE_DB", 4)

FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': CACHE_DEFAULT_TIMEOUT,
    'CACHE_KEY_PREFIX': 'superset_filter_cache_',
    'CACHE_REDIS_URL': f"redis://{REDIS_PASSWORD_PARAM}{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}"
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': CACHE_DEFAULT_TIMEOUT,
    'CACHE_KEY_PREFIX': 'superset_explore_cache_',
    'CACHE_REDIS_URL': f"redis://{REDIS_PASSWORD_PARAM}{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}"
}

# Configure the Flask rate limiter
RATELIMIT_STORAGE_URI = f"redis://{REDIS_PASSWORD_PARAM}{REDIS_HOST}:{REDIS_PORT}"

# Enabling proxy headers
ENABLE_PROXY_FIX = True

# Branding
APP_NAME = "Superset | Cohesion"
APP_ICON = "/static/assets/images/Cohesion_logo_RGB.png"
LOGO_TOOLTIP = "CohesionIB"
FAVICONS = [{"href": "/static/assets/images/Favicon_Cohesion.jpg"}]

# Theme adjustment
THEME_OVERRIDES = {
  "colors": {
    "primary": {
      "base": '#456BDE',
      "dark1": '#3756B2',
      "dark2": '#294085',
      "light1": '#6A89E5',
      "light2": '#8FA6EB',
      "light3": '#B5C4F2',
      "light4": '#DAE1F8',
      "light5": '#EDF1FC',
    }
  }
}

# Enable CORS
ENABLE_CORS = True
CORS_OPTIONS = {
      'supports_credentials': True,
      'allow_headers': ['*'],
      "expose_headers": ['*'],
      'resources': ['*'],
      'origins': ['cibdev-superset.nicedune-a486c6dd.centralus.azurecontainerapps.io', 'dev-insights.cohesionib.com']
    }