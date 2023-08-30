FROM python:3.10-slim

ARG ENV_NAME
WORKDIR /app

RUN apt update
RUN apt-get install build-essential -y #一部パッケージにgccが必要なため
RUN python3 -m pip install --upgrade pip

#RUN python3 -m pip install --no-cache-dir virtualenv
#RUN python3 -m venv $ENV_NAME
#RUN . /$ENV_NAME/bin/activate


COPY requirements.txt /.tmp/requirements.txt
RUN python3 -m pip install -r /.tmp/requirements.txt

COPY ./project.pth /usr/local/lib/python3.10/site-packages
