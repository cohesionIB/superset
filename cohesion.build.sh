#!/usr/bin/env bash

set -e

ACR_NAME=cibdevcontainers

echo "Building the Cohesion Apache Superset image"

build_number="$1"

if [ -z "$1" ]; then
    # Generate the build number based on the current date
    build_number="$(date +%Y%m%d).01"
fi

echo "Using the build number '$build_number'"
echo --------------------
echo "Logging in to the ACR"
az acr login --name "${ACR_NAME}"
echo --------------------
echo "Building the Apache Superset image"
docker build --platform=linux/amd64 -t "cib-superset:${build_number}" . -f cohesion.Dockerfile --no-cache
echo --------------------
echo "Tagging the Superset Docker image"
docker tag "cib-superset:${build_number}" "${ACR_NAME}.azurecr.io/superset:${build_number}"
echo --------------------
echo "Pushing the Superset Docker image to ACR"
docker push "${ACR_NAME}.azurecr.io/superset:${build_number}"
echo --------------------
echo "All done!"
echo --------------------
echo "Disclaimer: CohesionIB is pretty confident in its software and services, but if it happens to entirely accidentally turn your machine into a cold fusion reactor and open a giant hole in space that endangers the world as we know it, then Cohesion cannot in any way be made liable."