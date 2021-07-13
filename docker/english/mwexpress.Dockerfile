FROM python:3.8

RUN pip install nltk && python -c "import nltk; nltk.download('punkt');"

WORKDIR /app

COPY requirements.txt .

ENV TZ="Europe/London"
RUN apt-get update && apt-get install -y libpq-dev gcc tzdata

RUN pip install -r requirements.txt

COPY . ./

CMD [ "python", "./main.py" ]