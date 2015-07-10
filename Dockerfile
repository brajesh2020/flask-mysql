############################################################
# Dockerfile to build a container for a simple Flask app
############################################################

FROM python:2.7.8
ADD /flask-mysql /flask-mysql
RUN pip install -r /flask-mysql/requirements.txt
WORKDIR /flask-mysql
CMD ["python","app.py"]
EXPOSE 80