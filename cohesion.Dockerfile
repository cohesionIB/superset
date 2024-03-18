FROM --platform=linux/amd64 apache/superset:latest

WORKDIR /app

COPY --chown=superset:superset ./docker/pythonpath_dev/cohesion.superset_config.py ./pythonpath/superset_config.py
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Logo_Cohesion.png ./superset/static/assets/images/
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Favicon_Cohesion.jpg ./superset/static/assets/images/

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install psycopg2 pymssql pyodbc starrocks 'apache-superset[databricks]'
