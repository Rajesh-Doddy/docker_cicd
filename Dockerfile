FROM python:alpine3.19

RUN apk update
WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt
CMD ["python3","app.py"]
