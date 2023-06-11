#!/bin/bash
set -ex

# LOCAL_REGISTRY="registry.dev.appgoto.com"
LOCAL_REGISTRY="${LOCAL_REGISTRY:-registry.dev.appgoto.com}"

GIT_BRNCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse HEAD | cut -c 1-8)

IMAGE="${LOCAL_REGISTRY}/gfs-subscriber:${GIT_BRNCH}-${GIT_SHA}"
LATEST_IMAGE="${LOCAL_REGISTRY}/gfs-subscriber:latest"

docker build -t $IMAGE -f Dockerfile .
docker push $IMAGE
docker tag $IMAGE $LATEST_IMAGE
docker push $LATEST_IMAGE
