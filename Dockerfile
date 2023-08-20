FROM python:3.8

WORKDIR /app

COPY ./* /app/.

RUN ls -ltr

RUN pip install -r requirements.txt

RUN pip install -r requirements-dev.txt

RUN pre-commit install

COPY . .

#RUN ls -ltr

#CMD ["python3", "main.py"]
