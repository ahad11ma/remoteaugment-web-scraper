import scrapy
from my_scraper_project.items import MyScraperProjectItem  # Item class import ki

class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["quotes.toscrape.com"]  # Apni target website ka domain likhein
    start_urls = ["https://quotes.toscrape.com"]  # Jahan se scraping shuru karni hai

    def parse(self, response):
        # 1. BeautifulSoup ke soup.find_all() ki jagah Scrapy ka loop:
        for card in response.css('div.quote'):  # Apni website ka HTML tag/class likhein
            item = MyScraperProjectItem()
            
            # BeautifulSoup ke text nikalne ki jagah extract_first()
            item['title'] = card.css('span.text::text').extract_first()
            item['price'] = card.css('small.author::text').extract_first()
            item['link'] = response.urljoin(card.css('a::attr(href)').extract_first())
            
            # Data ko pipeline ki taraf bhejna
            yield item

        # 2. Pagination (Task Requirements: Scrape 3-5 pages)
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            # Agle page par request bhejna aur isi parse method ko dobara chalana
            yield scrapy.Request(next_page_url, callback=self.parse)