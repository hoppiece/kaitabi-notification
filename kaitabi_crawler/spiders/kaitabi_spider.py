import datetime
import json
import time
from string import Template

import scrapy
from items import KaitabiCrawlerItem
from scrapy.http import JsonRequest
from scrapy.linkextractors import LinkExtractor


class KaitabiSpider(scrapy.Spider):
    name = "kaitabi-spider"
    start_urls = ["https://www.hoshinoresorts.com/sp/kaitabi20s/"]

    resavation_extractor = LinkExtractor(allow=r"https:\/\/hoshinoresorts\.com\/plans\/JA/.+")

    def query_builder(self, hotelid, planid, month):
        epoch_ms = str(int(time.time() * 1000))
        url = (
            f"https://hoshinoresorts.com/api/rooms/vacancies/monthly?"
            f"hotelId={hotelid}&monthlyDate=2022%2F{month}%2F01&adult=2&underTwelve=0"
            f"&underSeven=0&underFour=0&stayLength=1&planId={planid}&lang=JA&_={epoch_ms}"
        )
        return url

    def parse(self, response):
        for hotel in response.xpath("//div[@class='body__listBlock js-accarea']"):
            url = hotel.xpath(".//li[@class='body__listBlockMainBtnItem']/a/@href").get()
            name = hotel.xpath("./button/span[@class='body__listBlockTriggerTxt']/text()").get()
            planid = url.split("/")[-1]
            hotelid = url.split("/")[-2]
            month = str(datetime.date.today().month + 2) # 2ヶ月後
            api = self.query_builder(hotelid, planid, month)
            yield JsonRequest(
                api, callback=self.parse_calender, cb_kwargs={"reservation_url": url, "name": name}
            )
            month = str(datetime.date.today().month + 3) # 3ヶ月後
            api = self.query_builder(hotelid, planid, month)
            yield JsonRequest(
                api, callback=self.parse_calender, cb_kwargs={"reservation_url": url, "name": name}
            )

    def parse_calender(self, response, reservation_url, name):
        jsonresponse = json.loads(response.text)
        vacancys = jsonresponse["vacancyList"]
        for day in vacancys:
            num_vacancy = day["vacancy"]
            if num_vacancy > 0:
                yield KaitabiCrawlerItem(
                    name=name,
                    reservation_url=reservation_url,
                    date=day["date"],
                    vacancy=num_vacancy,
                )
