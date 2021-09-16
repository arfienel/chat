FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /home/makek/DWS
COPY ./requirements.txt /home/makek/DWS
RUN pip install -r requirements.txt
COPY . /home/makek/DWS

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]