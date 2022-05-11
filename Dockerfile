FROM python:alpine

WORKDIR /shreddit
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN python setup.py install
VOLUME /config
WORKDIR /config

CMD ["/usr/local/bin/shreddit"]
