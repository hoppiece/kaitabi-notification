# Scrapy settings for kaitabi_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "kaitabi_crawler"

SPIDER_MODULES = ["kaitabi_crawler.spiders"]
NEWSPIDER_MODULE = "kaitabi_crawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_ENABLED = False

FEEDS = {
    "stdout:": {"format": "csv", "encoding": "utf-8"},
    "/tmp/kaitabi_out.json": {"format": "json", "encoding": "utf-8"},
}
DOWNLOADER_CLIENT_TLS_METHOD = "TLS"
