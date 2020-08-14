from scrapy import Spider
from scrapy.selector import Selector

from hackernews.items import HackernewsItem


class BasicSpider(Spider):
    # name the spider
    name = "basic"

    # allowed domains to scrape
    allowed_domains = ["news.ycombinator.com"]

    # urls the spider begins to crawl from
    start_urls = ['https://news.ycombinator.com/']

    # parses and returns the scraped data
    def parse(self, response):
        titles = Selector(response).xpath('//tr[@class="athing"]/td[3]')  # finds the third <td> after the element with

        for title in titles:
            item = HackernewsItem()
            item['title'] = title.xpath("a[@href]/text()").extract()  # finds all <a> tags within each <td> tag, then extracts the text
            item['url'] = title.xpath("a/@href").extract()  # again finds all <a> tags within each <td> tag, but this time it extracts the actual url
            yield item
