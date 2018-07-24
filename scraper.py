import scrapy

class HolidaySpider(scrapy.Spider):
    name = "holiday_spider"
    start_urls = ['https://www.bot.or.th/Thai/FinancialInstitutions/FIholiday/Pages/2018.aspx']

    def parse(self, response):

        holiday_table = response.xpath('//*[@id="WebPartWPQ1"]/div[1]/table[2]/tbody/tr')

        for row in holiday_table:
            name = {
                'week_day' : row.xpath('td[2]//text()').extract_first(),
                'date': row.xpath('td[3]//text()').extract_first(),
                'month' : row.xpath('td[4]//text()').extract_first(),
                'desc' : row.xpath('td[5]//text()').extract_first()
            }
            self.log(name)

        