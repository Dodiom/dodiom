FROM python:3
WORKDIR /app

COPY src/requirements.txt .
RUN pip install -r requirements.txt
RUN python -c "import stanza; stanza.download('en'); stanza.download('tr')"

COPY src ./
CMD [ "python", "./main.py" ]