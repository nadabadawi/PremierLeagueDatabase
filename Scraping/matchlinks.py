import scrapy


class MatchlinksSpider(scrapy.Spider):
    name = 'matchlinks'
    def start_requests(self):
        urls = [
            'https://www.premierleague.com/results?co=1&se=418&cl=-1',
            'https://www.premierleague.com/results?co=1&se=363&cl=-1',
            'https://www.premierleague.com/results?co=1&se=274&cl=-1',
            'https://www.premierleague.com/results?co=1&se=210&cl=-1'
    	]
        	
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        hello = open("links.txt", "a")
        for match in response.xpath('//li[@class="matchFixtureContainer"]'):
            hello.write(match.css('div.fixture.postMatch::attr(data-href)').get() + "\n")
            # OR
            #hello.write(match.xpath('//div[@class="fixture postMatch"]/@data-href()').get() + "\n")
        hello.close()