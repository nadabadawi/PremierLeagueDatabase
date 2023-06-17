import scrapy


class Matchspy2Spider(scrapy.Spider):
    name = 'matchspy2'
    def start_requests(self):
        urls = [
            'https://www.premierleague.com/match/66355'
    	]
        	
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
         for match in response.css('div.centralContent'):
            goal = match.css('.fullTime::text').extract()
            yield{
				'Home Club Team': match.css('.home .long::text').extract(),
                'Home Goals': goal[0],
                'Away Goals': goal[1],
                'Away Club Team': match.css('.away .long::text').extract(),
                'Date': match.css('div.matchDate.renderMatchDateContainer::text').extract(),
                'Stadium': match.css('div.stadium::text').extract(),
            }
