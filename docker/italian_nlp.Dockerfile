FROM openjdk:16-slim

WORKDIR /home

RUN apt-get update && apt-get install -y wget
RUN wget http://www.airpedia.org/tint/1.0-SNAPSHOT/tint-runner-1.0-SNAPSHOT-bin.tar.gz
RUN tar xzf tint-runner-1.0-SNAPSHOT-bin.tar.gz && mv tint/* .

CMD sh ./tint-server.sh