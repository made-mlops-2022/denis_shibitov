FROM python:3.7-slim-stretch
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY split.py /split.py

ENTRYPOINT ["python", "split.py"]