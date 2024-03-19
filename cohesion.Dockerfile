FROM --platform=linux/amd64 apache/superset:latest

USER root

COPY --chown=superset:superset ./docker/pythonpath_dev/cohesion.superset_config.py ./pythonpath/superset_config.py
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Cohesion_logo_RGB.png ./superset/static/assets/images/
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Favicon_Cohesion.jpg ./superset/static/assets/images/

RUN pip install --no-cache-dir psycopg2 pymssql pyodbc starrocks 'apache-superset[databricks]'

USER superset
