FROM python:3.8

WORKDIR /app

COPY * .

RUN ls -ltr

RUN pip3 install -r requirements-dev.txt

RUN pre-commit install

COPY . .

#RUN ls -ltr

#CMD ["python3", "main.py"]
