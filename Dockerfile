FROM python:3

COPY . /cotacao

RUN pip install flask && pip install requests

WORKDIR  /cotacao

EXPOSE 5000

CMD ["python", "main.py"]
