import csv

class MyScraperProjectPipeline:
    def open_spider(self, spider):
        # Spider start hote hi CSV file create karna
        self.file = open('output_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        # Header row likhna
        self.writer.writerow(['Title', 'Price', 'Link'])

    def process_item(self, item, spider):
        # Har scrape hone wale item ko CSV me write karna
        self.writer.writerow([item.get('title'), item.get('price'), item.get('link')])
        return item

    def close_spider(self, spider):
        # Spider khatam hote hi file close karna
        self.file.close()