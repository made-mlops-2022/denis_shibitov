FROM python:3.7-slim-stretch
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py person_parameters.py ./

WORKDIR .

ENV MODEL_PATH="https://disk.yandex.ru/d/CtY5RxXyYn6hfQ"

EXPOSE 4242

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4242"]
