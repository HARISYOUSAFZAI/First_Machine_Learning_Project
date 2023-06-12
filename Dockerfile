FROM python:3.8
COPY . /app
WORKDIR /app
<<<<<<< HEAD
RUN pip install -r requirement.txt
EXPOSE $PORT   
CMD gunicorn --workers=4 --bind 0.0.0.0:$port app:app
=======
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
>>>>>>> 684f333b9c3e48f4a7efec599603c045abc86dfe
