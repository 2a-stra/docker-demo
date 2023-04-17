FROM python:3.11-alpine

WORKDIR /home/app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8888

CMD ["python", "main.py"]
