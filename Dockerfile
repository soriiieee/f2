FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y
# flask をコンテナにinstall
RUN pip3 install flask