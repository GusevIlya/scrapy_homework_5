import scrapy
from scrapy.http import HtmlResponse
from labirint_books.items import LabirintBooksItem

class LabirintSpider(scrapy.Spider):
    name = "detectives"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/genres/2498"]

    def parse(self, response: HtmlResponse):

        links = response.xpath("//div[@class='inner-catalog']//a[@class='product-title-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.books_parse)

        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            response.follow(next_page, callback=self.parse)

    def books_parse(self, response: HtmlResponse):
        _id = response.url
        autor = response.xpath("//div[@id='product-title']/h1/text()").get()
        title = response.xpath("//div[@id='product-title']/h1/text()").get()
        publisher = response.xpath("//a[@data-event-label='publisher']/@data-event-content").get()
        year = response.xpath("//div[@class='publisher']/text()").getall()
        price = response.xpath("//span[@class='buying-pricenew-val-number']/text()").get()
        yield LabirintBooksItem(_id=_id, autor=autor, title=title, publisher=publisher, year=year, price=price)
