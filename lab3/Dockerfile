FROM python:3.11-alpine

WORKDIR /app
ADD app.py .

ADD requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 8888

CMD ["gunicorn", "--bind", "0.0.0.0:8888", "app:app"]
