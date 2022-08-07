FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./chromedriver /usr/local/bin/chromedriver
COPY ./chromedriver /usr/local/bin/chromedriver
RUN apt-get update && apt-get install -y curl xvfb unzip xvfb libxi6 libgconf-2-4  \
    chromium
RUN chmod +x /usr/local/bin/chromedriver
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code