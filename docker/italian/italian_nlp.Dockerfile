FROM openjdk:16-slim

WORKDIR /home

RUN apt-get update && apt-get install -y wget
RUN wget https://dhsite.fbk.eu/tint-release/0.3/tint-0.3-complete.tar.gz
RUN tar xzf tint-0.3-complete.tar.gz && mv tint/* .

CMD sh ./tint-server.sh