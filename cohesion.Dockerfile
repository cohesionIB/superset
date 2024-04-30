FROM --platform=linux/amd64 apache/superset:latest

USER root

COPY --chown=superset:superset ./docker/pythonpath_dev/cohesion.superset_config.py ./pythonpath/superset_config.py
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Cohesion_logo_RGB.png ./superset/static/assets/images/
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Favicon_Cohesion.jpg ./superset/static/assets/images/

COPY --chmod=755 ./docker/run-server.sh /usr/bin/

RUN pip install --no-cache-dir databricks-sql-connector==2.9.5 sqlalchemy-databricks==0.2.0 apache-superset[cors] duckdb duckdb-engine

USER superset
