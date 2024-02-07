FROM python:3.11.7-slim

ENV PYTHONUNBUFFERED 1 # Force the stdout and stderr streams to be unbuffered.
EXPOSE 8000
WORKDIR /

COPY ./requirements.txt .
COPY ./tailwind.config.js .
COPY ./app app

RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]
