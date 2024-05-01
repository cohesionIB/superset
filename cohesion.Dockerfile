FROM --platform=linux/amd64 apache/superset:latest

USER root

COPY --chown=superset:superset ./docker/pythonpath_dev/cohesion.superset_config.py ./pythonpath/superset_config.py
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Cohesion_logo_RGB.png ./superset/static/assets/images/
COPY --chown=superset:superset ./superset-frontend/src/assets/images/Favicon_Cohesion.jpg ./superset/static/assets/images/
COPY --chown=superset:superset ./superset/templates/superset/cohesion.basic.html ./superset/templates/superset/basic.html

COPY --chmod=755 ./docker/run-server.sh /usr/bin/

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget && \
    apt-get install -y --no-install-recommends unzip && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb && \
    rm -f google-chrome-stable_current_amd64.deb

# RUN export CHROMEDRIVER_VERSION=$(curl --silent https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
#     wget -q https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
#     unzip chromedriver_linux64.zip -d /usr/bin && \
#     chmod 755 /usr/bin/chromedriver && \
#     rm -f chromedriver_linux64.zip

RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/linux64/chromedriver-linux64.zip && \
    unzip -j chromedriver-linux64.zip -d /usr/bin && \
    chmod 755 /usr/bin/chromedriver && \
    rm -f chromedriver-linux64.zip

RUN pip install --no-cache-dir databricks-sql-connector==2.9.5 sqlalchemy-databricks==0.2.0 apache-superset[cors] duckdb duckdb-engine authlib prophet psycopg2 gevent redis

RUN mkdir -p /mnt/data \
    && chown -R superset:superset /mnt/data

RUN mkdir -p /mnt/data \
    && chown -R superset:superset /mnt/data

USER superset
