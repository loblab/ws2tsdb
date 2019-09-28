FROM python:3.7
MAINTAINER loblab

ARG APT_MIRROR=mirrors.163.com
ARG DEBIAN_FRONTED=noninteractive
RUN find /etc/apt -type f -name "*.list" -exec sed -i s/deb.debian.org/$APT_MIRROR/ {} \;
RUN find /etc/apt -type f -name "*.list" -exec sed -i s/security.debian.org/$APT_MIRROR/ {} \;
RUN apt-get update --fix-missing && apt-get -y upgrade

ARG PYTHON=python3
RUN apt-get -y install ${PYTHON}-pip
RUN $PYTHON -m pip install --upgrade pip

RUN $PYTHON -m pip install websockets
RUN $PYTHON -m pip install influxdb

