#!/bin/bash

docker-compose down && \
docker build -t atareao/wallabot:amd64 . && \
docker-compose up -d && \
docker-compose logs -f
