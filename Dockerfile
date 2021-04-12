FROM python:3.7-alpine


ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
RUN apk --update add redis 

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev \
    && RUN apk add zlib-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk del build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user