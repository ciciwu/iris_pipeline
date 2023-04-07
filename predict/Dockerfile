# docker run -v /Users/congwu/Documents/Projects/iris/model/output:/app/output {targetname}
FROM python:3.7 as base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir  /app/output
COPY predict.py predict.py

#FROM base as test
#RUN ["pytest", "test_model_train.py"]


FROM base as build
CMD ["python", "predict.py"]
