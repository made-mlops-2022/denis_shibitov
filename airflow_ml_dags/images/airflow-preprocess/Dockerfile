FROM python:3.7-slim-stretch
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY preprocess.py /preprocess.py

ENTRYPOINT ["python", "preprocess.py"]