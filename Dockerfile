FROM python:3.8

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY ./ .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "app.py" ]