from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from socrata.items import SocrataItem


class OpendataSpider(CrawlSpider):
    name = "oopendata_crawl"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = ['https://opendata.socrata.com/']

    # LinkExtractor specifies the links that should be crawled
    # allow parameter defines regular expression the URL must match in order to be crawled
    rules = [
        Rule(LinkExtractor(allow='browse\?utf8=%E2%9C%93&page=\d*'),
             callback='parse_item', follow=True)
    ]

    def parse(self, response):
        titles = Selector(response).xpath('//div[@itemscope="itemscope"]')
        for title in titles:
            item = SocrataItem()
            item["text"] = title.xpath('.//div[@class="browse2-result-title"]/h2/a/text()').extract()[0]
            item["url"] = title.xpath('.//div[@class="browse2-result-title"]/h2/a/@href').extract()[0]
            item["views"] = title.xpath('.//div[@class="browse2-result-view-countvalue"]/text()').extract()[0].strip()
            yield item

