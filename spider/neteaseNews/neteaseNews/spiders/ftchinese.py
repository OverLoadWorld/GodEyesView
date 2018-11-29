import scrapy

class ftchinese(scrapy.Spider): #需要继承scrapy.Spider类

    name = "ftchinese" # 定义蜘蛛名
    allowed_domains = ["www.ftchinese.com/channel/"]
    start_urls = ['http://www.ftchinese.com/channel/china.html?page=100']

    def parse(self, response):
        items = response.xpath("//div[@class='item-inner']")
        for i in items:
            title = i.xpath("h2[@class='item-headline']/a/text()").extract()
            url = i.xpath("h2[@class='item-headline']/a/@href").extract()
            time = i.xpath("div[@class='item-time']/text()").extract()
            if(title):
                print(title, ' - ',  time, ' - ', url)
        pre_page = response.xpath("//div[@class='pagination-inner']/a[2]/@href").extract_first()
        pre_page = response.urljoin(pre_page)
        print(pre_page)
        # 001080420 001000104
        # 001080420 001000104
