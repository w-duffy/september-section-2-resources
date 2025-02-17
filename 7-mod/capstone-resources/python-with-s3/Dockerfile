FROM python:3.9

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install psycopg2

COPY . .

CMD flask db upgrade && flask seed all && gunicorn app:app
