FROM debian:12

RUN apt update -y && apt install -y rsync python3 openssh-client

RUN adduser --disabled-password --gecos "" rsync

USER rsync

WORKDIR /app
COPY *.py ./

ENTRYPOINT ["python3", "main.py"]