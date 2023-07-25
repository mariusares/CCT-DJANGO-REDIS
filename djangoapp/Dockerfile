FROM python:3.10.11-bullseye
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev libpq-dev curl
RUN pip install --upgrade pip
RUN pip install dnspython install django gunicorn redis
ENV LIBRARY_PATH=/lib:/usr/lib
WORKDIR /app
COPY . /app
CMD gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000
