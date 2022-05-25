FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /django
COPY requirements.txt /django/
RUN pip3 install -r requirements.txt
RUN pip3 install djangorestframework --upgrade
COPY . /django/
