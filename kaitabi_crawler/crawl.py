import json
import os
from multiprocessing import Process

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.kaitabi_spider import KaitabiSpider


def do_crawl():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(KaitabiSpider)
    process.start()


def run():
    process = Process(target=do_crawl)
    process.start()
    process.join()
    with open("/tmp/kaitabi_out.json") as fp:
        result = json.load(fp)
    os.remove("/tmp/kaitabi_out.json")
    response = {"statusCode": 200, "results": result}
    return response


if __name__ == "__main__":
    run()
