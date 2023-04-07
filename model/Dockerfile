# docker run -v /Users/congwu/Documents/Projects/iris/model/output:/app/output {targetname}
FROM python:3.7 as base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir  /app/output
COPY model_train.py model_train.py
COPY test_model_train.py test_model_train.py

FROM base as test
RUN ["pytest", "test_model_train.py"]

FROM base as build
CMD ["python", "model_train.py"]
