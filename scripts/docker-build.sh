#!/bin/bash

docker build -t zaslavskyd/od-search:$1 .
docker build -t zaslavskyd/od-search:latest .
