FROM python:3.9-slim-buster


WORKDIR /home/notify

RUN pip install --upgrade pip
COPY ./requirements.txt /home/notify/requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]