import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'rating': book.css('p.star-rating::attr(class)').get().split()[-1],
                'availability': book.css('p.instock.availability::text').getall()[-1].strip(),
                'url': response.urljoin(book.css('h3 a::attr(href)').get()),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
