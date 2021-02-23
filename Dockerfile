FROM python:3.9-slim-buster
ENV AWS_DEFAULT_REGION='us-east-1'
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get clean &&\
    apt-get update &&\
    apt-get install --assume-yes --fix-missing\
    openssh-server git
# NOTE uncomment if we need ssh access into the container (probably won't)
# RUN echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config
# RUN /etc/init.d/ssh start

COPY requirements.txt /var/requirements.txt
RUN pip install -r /var/requirements.txt
