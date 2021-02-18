FROM ubuntu:latest


ARG project_dir=/home
RUN apt-get update
RUN apt-get install python3 python3-pip -y
# flask をコンテナにinstall
# RUN pip3 install flask
ADD requirements.txt $project_dir
ADD hello.py $project_dir

RUN pip3 install -r requirements.txt --no-cache-dir