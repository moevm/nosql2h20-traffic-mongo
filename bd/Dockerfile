FROM mongo:latest

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7-dev
RUN pip3 install pymongo==3.11.0

RUN pwd

COPY . .

RUN mongod --bind_ip_all & (python3 ./import_osm.py ./map && mongod --shutdown)

EXPOSE 27017