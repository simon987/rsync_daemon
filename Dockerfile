FROM debian:12

RUN apt update -y && apt install -y rsync python3

WORKDIR /app
COPY *.py ./

ENTRYPOINT ["python3", "main.py"]