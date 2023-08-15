FROM python:3.10-slim

ARG ENV_NAME
WORKDIR /app

RUN python3 -m pip install --upgrade pip

#RUN python3 -m pip install --no-cache-dir virtualenv
#RUN python3 -m venv $ENV_NAME
#RUN . /$ENV_NAME/bin/activate

# Jupyterだけは起動に必要なので先んじてインストール
RUN python3 -m pip install --no-cache-dir jupyter
