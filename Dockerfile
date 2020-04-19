FROM python:3.7

WORKDIR /flaskapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pytest

# add metadata that port 8080 is accessible
EXPOSE 8080

CMD FLASK_APP=romanflask/flask_app.py flask run --host=0.0.0.0 --port=8080