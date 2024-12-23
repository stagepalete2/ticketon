FROM python:3.12

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev \
    libpq-dev gettext cron flake8 locales vim

WORKDIR /app

ADD ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt gunicorn


COPY . .

EXPOSE 9000


CMD ["bash", "-c", "gunicorn -b 0.0.0.0:9000 ticketon.wsgi:application"]

