# syntax=docker/dockerfile:1

FROM python:3.9.6-alpine

LABEL maintainer="brianmoyou@gmail.com"

EXPOSE 5000

WORKDIR /app

ENV FLASK_APP /app/main.py

ENV FLASK_ENV=development

# ENTRYPOINT ["./gunicorn.sh"]

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
