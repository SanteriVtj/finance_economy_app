FROM python:3.8

WORKDIR /project
ADD . /project
RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

CMD ["app.py"]