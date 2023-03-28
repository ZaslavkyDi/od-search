#!/bin/bash

docker image tag od-search:$1 zaslavskyd/od-search:$1
docker image push zaslavskyd/od-search:$1

# Update latest docker version with the current build
docker image tag od-search:latest zaslavskyd/od-search:latest
docker image push zaslavskyd/od-search:latest
