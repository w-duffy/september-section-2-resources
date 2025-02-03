# This builds an image for a hello world flask app

FROM python:3.9

# WORKDIR /usr/local/app
# WORKDIR /var/www/app
WORKDIR /tacos
# CMD ["tail", "-f", "/dev/null"]

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
