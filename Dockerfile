FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir  /app/output
COPY model model

CMD ["python", "model/model_train.py"]
