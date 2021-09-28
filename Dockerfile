FROM python:3.9.0

WORKDIR /home/

RUN echo 'sacxacs'

RUN git clone https://github.com/ui-hyeong/gis_3class.git

WORKDIR /home/gis_3class/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c","python manage.py collectstatic --noinput --settings=GIS_P.settings.deploy && python manage.py migrate --settings=GIS_P.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=GIS_P.settings GIS_P.wsgi --bind 0.0.0.0:8000"]
