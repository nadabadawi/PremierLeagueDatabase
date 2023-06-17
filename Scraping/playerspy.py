import scrapy


class PlayerspySpider(scrapy.Spider):
    name = 'playerspy'
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
        # links = open('Players.txt', 'a')
        #list = []
        #file=open("hello.txt")
        hello = open("players22.txt", "a")
        for player in response.css('a.playerOverviewCard.active'):
            
            print("HERE")
            hello.write("https://www.premierleague.com" + player.css('a.playerOverviewCard.active::attr(href)').get() + "\n")
            #list.append(player.css('a.playerOverviewCard.active::attr(href)')).get()
            yield{
				'Player Number': player.css('span.number::text').get(),
                'Name': player.css('h4.name::text').get(),
                'Position': player.css('span.position::text').get(),
            }
        hello.close()
        




















        # hyperlk = player.css('a.playerOverviewCard.active::attr(href)').get()
        # hyperlk = player.urljoin(hyperlk)
        # file = open("write4.txt", "a")
        # file.write(hyperlk + "\n")
        # file.close()
            # links.write("Test File\n")
            # links.write(response.urljoin('https://www.premierleague.com', response.css('a.playerOverviewCard.active::attr(href)')).get())
        #print(list)

       
#Comments:
# 'Club Name': player.css('h1.team\ js-team::text').get(),
                # 'Nationality': player.css('span.playerCountry::text').get()
                # 'Date of Birth': player.css().get(),
                # # 'Weight': player.css().get(),
                # 'Height': player.css().get()
 # for player in response.css('ul.squadPlayerStats'):
        #     yield{
        #         'Nationality': player.css('span.playerCountry::text').get()
        #     }
        # next_page = response.css('a.playerOverviewCard\ active::attr(href)').get()
        # next_page = response.urljoin(next_page)
        # yield scrapy.Request(next_page, callback=self.parse)
