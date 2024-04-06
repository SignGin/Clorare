FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/server
ADD . /srv/server

WORKDIR /srv/server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]