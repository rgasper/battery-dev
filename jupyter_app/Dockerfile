FROM python:3.9-slim-buster
ENV AWS_DEFAULT_REGION='us-east-1'
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# NOTE uncomment if you need to install apps
# RUN apt-get clean &&\
#     apt-get update &&\
#     apt-get install --assume-yes --fix-missing\
#     openssh-server iputils-ping graphviz
# NOTE uncomment if we need ssh access into the container (probably won't)
# RUN echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config
# RUN /etc/init.d/ssh start

RUN mkdir /jupyter_app

COPY requirements.txt /jupyter_app/requirements.txt
RUN pip install -r /jupyter_app/requirements.txt

WORKDIR /jupyter_app
ADD . /jupyter_app/

CMD [ "bash", "/jupyter_app/entrypoint.sh" ]
