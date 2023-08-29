FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./main.py /app/main.py

VOLUME ./main.py

ENV AUTHOR=Fanis
ENV UUID=bd65600d-8669-4903-8a14-af88203add38

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

