FROM python:3.9

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED True
# ENV PYTHONUNBUFFERED="True"
# ENV GECKODRIVER_VER v0.29.0
# ENV FIREFOX_VER 87.0
COPY . /app
WORKDIR /app

# RUN mkdir __logger

RUN apt-get install wget

RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
       firefox-esr 
 
# Add latest FireFox
RUN set -x \
   && apt install -y \
       libx11-xcb1 \
       libdbus-glib-1-2 \
   && curl -sSLO https://ftp.mozilla.org/pub/firefox/releases/92.0/linux-x86_64/en-US/firefox-92.0.tar.bz2 \
   && tar -jxf firefox-* \
   && mv firefox /opt/ \
   && chmod 755 /opt/firefox \
   && chmod 755 /opt/firefox/firefox
  
# Add geckodriver
RUN set -x \
   && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/


RUN pip install --upgrade pip

RUN pip install -r requirements.txt
ENV PORT 8080

# CMD [ "gunicorn", "--workers=1", "--threads=1", "-b 0.0.0.0:8080","--graceful-timeout 100", "app:app"]
CMD gunicorn --timeout 1000 --workers 1 --threads 4 --bind 0.0.0.0:8080 main:app
# --log-level debug
# CMD["gunicorn", "--timeout", "1000", "--workers=1","-b", "0.0.0.0:8000","--log-level", "debug", "manage"]
