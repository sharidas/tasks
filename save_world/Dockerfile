From ubuntu:20.04

RUN apt-get update

RUN apt-get install -y python3 python3-virtualenv libpq-dev python-dev-is-python3 python3.8-dev build-essential

WORKDIR /usr/src/app

ENV VIRTUALENV /opt/env
RUN virtualenv --python python3 ${VIRTUALENV}

ENV PATH="${VIRTUALENV}/bin:$PATH"

COPY ./requirements.txt /usr/src/app

RUN ls -l /usr/src/app/

RUN pip install -r requirements.txt

COPY . /usr/src/app

ENV FLASK_APP /usr/src/app/wsgi.py
ENV FLASK_ENV production

ENTRYPOINT python manage.py create_db && gunicorn --bind 0.0.0.0:8080 wsgi:app
