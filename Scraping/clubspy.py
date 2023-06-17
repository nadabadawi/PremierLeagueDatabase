import scrapy


class ClubspySpider(scrapy.Spider):
    name = 'clubspy'
    def start_requests(self):
        urls = [
                'https://www.premierleague.com/clubs/1/club/squad',
                'https://www.premierleague.com/clubs/2/club/squad',
                'https://www.premierleague.com/clubs/130/club/squad',
                'https://www.premierleague.com/clubs/131/club/squad',
                'https://www.premierleague.com/clubs/43/club/squad',
                'https://www.premierleague.com/clubs/4/club/squad',
                'https://www.premierleague.com/clubs/6/club/squad',
                'https://www.premierleague.com/clubs/7/club/squad',
                'https://www.premierleague.com/clubs/9/club/squad',
                'https://www.premierleague.com/clubs/26/club/squad',
                'https://www.premierleague.com/clubs/10/club/squad',
                'https://www.premierleague.com/clubs/11/club/squad',
                'https://www.premierleague.com/clubs/12/club/squad',
                'https://www.premierleague.com/clubs/23/club/squad',
                'https://www.premierleague.com/clubs/14/club/squad',
                'https://www.premierleague.com/clubs/20/club/squad',
                'https://www.premierleague.com/clubs/21/club/squad',
                'https://www.premierleague.com/clubs/33/club/squad',
                'https://www.premierleague.com/clubs/25/club/squad',
                'https://www.premierleague.com/clubs/38/club/squad'
    	]
        	
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for club in response.css('div.clubDetailsContainer'):
            yield{
				'Club Name': club.css('h1.team.js-team::text').getall(),
                'Website': club.css('a::text').getall()
            }
	
        # next_page = response.css('a.playerOverviewCard\ active::attr(href)').get()
        # next_page = response.urljoin(next_page)
        # yield scrapy.Request(next_page, callback=self.parse)

