FROM pytorch/pytorch

RUN pip install stanza && python -c "import stanza; stanza.download('en'); stanza.download('tr')"

WORKDIR /app

COPY requirements.txt .

ENV TZ="Europe/Istanbul"
RUN apt-get update && apt-get install -y libpq-dev gcc tzdata

RUN pip install -r requirements.txt

COPY . ./
RUN pip install nlp/cupt-parser

CMD [ "python", "./main.py" ]