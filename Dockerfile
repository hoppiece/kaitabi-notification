FROM python:3.9

WORKDIR /opt

COPY kaitabi_crawler kaitabi_crawler
COPY scrapy.cfg .
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /opt/kaitabi_crawler
CMD ["python", "crawl.py"]