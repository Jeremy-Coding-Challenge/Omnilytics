FROM python:3.7.6-stretch

WORKDIR /usr/src/app


COPY . .

CMD [ "python", "./challenge_b.py"]