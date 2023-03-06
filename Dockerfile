FROM python:3.9-slim-buster

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
    


ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt ./


RUN python -m pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]