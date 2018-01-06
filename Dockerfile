FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /capritools
WORKDIR /capritools
ADD requirements.txt /capritools
RUN pip install -r requirements.txt
ADD . /capritools
ADD import.py /capritools
ADD docker-entrypoint.sh /capritools

#RUN python manage.py migrate
#RUN python import.py

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["sh",  "docker-entrypoint.sh"]
