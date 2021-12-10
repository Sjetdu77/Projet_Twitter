FROM alpine:3
RUN mkdir ./app
WORKDIR ./app
RUN apk update && apk add python3 py3-pip
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "./main.py"]