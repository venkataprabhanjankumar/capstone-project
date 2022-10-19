FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN export GOOGLE_APPLICATION_CREDENTIALS=/code/secret.json

RUN echo "${GOOGLE_APPLICATION_CREDENTIALS=/code/secret.json}"

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]