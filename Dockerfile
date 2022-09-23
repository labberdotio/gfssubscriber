
# 
# https://runnable.com/docker/python/dockerize-your-flask-application
# 
# > docker build -t gfsrippler:latest -f Dockerfile.server .
# > docker network create -d bridge gremlinfs
# > docker run -d -e ... --net=gremlinfs -p 5000:5000 gfsrippler:latest
# 

# 
# Alpine latest installs python 3.8, we need 3.6
# 
# FROM alpine:latest
FROM alpine:3.9

# ENV
ENV GFS_NAMESPACE="gfs1"
ENV GFS_PUSHER_HOST="gfs-pusher"
ENV GFS_PUSHER_PORT="5002"
# ENV GFS_PUSHER_USERNAME="root"
# ENV GFS_PUSHER_PASSWORD="root"

USER root

RUN apk update

# c/_cffi_backend.c:15:10: fatal error: ffi.h: No such file or directory
# #include <ffi.h>
Run apk add --update libffi-dev

# Install python
# RUN apk add --update \
#     python3 \
#     python3-dev \
#     py-pip \
#     build-base \
#   && pip install virtualenv \
#   && rm -rf /var/cache/apk/*
RUN apk add --update \
    python3 \
    python3-dev \
    py-pip \
    build-base \
  && rm -rf /var/cache/apk/*

ADD ./ /app

WORKDIR /app

# Addl. python 
# RUN pip install -r ./requirements.txt
RUN pip3 install -r ./requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "./subscriber.py" ]

