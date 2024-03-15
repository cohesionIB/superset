import os
from datetime import timedelta

####################################################################################
#
# Initial Cohesion Dev environment config
#
####################################################################################

# Set the secret key
# Make sure to set the secret key in the SUPERSET_SECRET_KEY environment variable

# Set the Flask debug flag
# Make sure to the the Flask debug flag in the FLASK_DEBUG environment variable

# Make sure to specify all attributes of the metastore DB in environment variables specified below
# SQLALCHEMY_DATABASE_URI = (
#    f"{DATABASE_DIALECT}://"
#    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
#    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
#)

# Disabling Python stack traces by default
SHOW_STACKTRACE = os.environ.get("SHOW_STACKTRACE", False)

# Enable alerts and reports
FEATURE_FLAGS = {"ALERT_REPORTS": True}

# Cache configuration
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CACHE_DB = os.environ.get("REDIS_CACHE_DB", 4)

FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': int(timedelta(hours=24).total_seconds()),
    'CACHE_KEY_PREFIX': 'superset_filter_cache_',
    'CACHE_REDIS_URL': f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}"
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': int(timedelta(hours=24).total_seconds()),
    'CACHE_KEY_PREFIX': 'superset_explore_cache_',
    'CACHE_REDIS_URL': f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}"
}

# Configure the Flask rate limiter
RATELIMIT_STORAGE_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}"

# Enable template processing
FEATURE_FLAGS = {"ENABLE_TEMPLATE_PROCESSING": True}

# Enabling proxy headers
ENABLE_PROXY_FIX = True