import os
from datetime import timedelta

####################################################################################
#
# Initial Cohesion Dev environment config
#
####################################################################################

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