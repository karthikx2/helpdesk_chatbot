FROM python:3.8

WORKDIR /app

COPY ./ /app

RUN ls -ltr

RUN pip install -r requirements.txt

RUN pip install -r requirements-dev.txt

RUN pre-commit install

COPY . .

RUN chmod 777 nlu_startup.sh

RUN ls -ltr 

ENTRYPOINT ["/app/nlu_startup.sh"]

EXPOSE 5005
