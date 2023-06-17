import scrapy
import re


class StadiumspySpider(scrapy.Spider):
    name = 'stadiumspy'

    def start_requests(self):
        urls = [
                'https://www.premierleague.com/clubs/1/club/stadium',
                'https://www.premierleague.com/clubs/2/club/stadium',
                'https://www.premierleague.com/clubs/130/club/stadium',
                'https://www.premierleague.com/clubs/131/club/stadium',
                'https://www.premierleague.com/clubs/43/club/stadium',
                'https://www.premierleague.com/clubs/4/club/stadium',
                'https://www.premierleague.com/clubs/6/club/stadium',
                'https://www.premierleague.com/clubs/7/club/stadium',
                'https://www.premierleague.com/clubs/9/club/stadium',
                'https://www.premierleague.com/clubs/26/club/stadium',
                'https://www.premierleague.com/clubs/10/club/stadium',
                'https://www.premierleague.com/clubs/11/club/stadium',
                'https://www.premierleague.com/clubs/12/club/stadium',
                'https://www.premierleague.com/clubs/23/club/stadium',
                'https://www.premierleague.com/clubs/14/club/stadium',
                'https://www.premierleague.com/clubs/20/club/stadium',
                'https://www.premierleague.com/clubs/21/club/stadium',
                'https://www.premierleague.com/clubs/33/club/stadium',
                'https://www.premierleague.com/clubs/25/club/stadium',
                'https://www.premierleague.com/clubs/38/club/stadium'
    	]
        	
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for stadium in response.css('div.clubDetails'):
            #name = stadium.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "stadium", " " ))]/text()').get()
            club = str(stadium.css('h1.team.js-team::text').extract())
            club = club.replace(']', '')
            club = club.replace('[', '')
            club = club.replace('\'', '')
            # delete = stadium.css('div.stadiumName').getall()
            # print("Delete is here!!",delete)
            # print("HELLO")
            # #print(name)
            # print()
            # yield{
            #     'Name': name,
            #     'Club': club,
            # }
        for stadium in response.xpath('//div[@data-ui-tab="Stadium Information"]'):
            # cap = stadium.css('p:nth-child(1)::text').extract()
            # cap = re.sub(r"[\n\t\s]*", "", cap)

            nm = str(stadium.css('h2::text').getall())
            cap = str(stadium.css('p:nth-child(1)::text').extract())
            #@tag_name --> href
            lbl = str(stadium.css('p:nth-child(2) strong:nth-child(1)::text').extract())
            att = str(stadium.css('p:nth-child(2)::text').extract())
            Bdate = str(stadium.css('p:nth-child(3)::text').extract())
            Psize = str(stadium.css('p:nth-child(4)::text').extract())
            add = str(stadium.css('p:nth-child(5)::text').extract())
            
            name = nm.replace('\\xa0', '')
            name = name.replace(']', '')
            name = name.replace('[', '')
            name = name.replace('\'', '')
            capacity = cap.replace('\\xa0', '')
            capacity = capacity.replace(']', '')
            capacity = capacity.replace('\'', '')
            capacity = capacity.replace('[', '')
            capacity = capacity.replace(',', '')
            attendance = att.replace('\\xa0', '')
            attendance = attendance.replace(']', '')
            attendance = attendance.replace('\'', '')
            attendance = attendance.replace('[', '')
            attendance = attendance.replace(',', '')
            build_date = Bdate.replace('\\xa0', '')
            build_date = build_date.replace(']', '')
            build_date = build_date.replace('\'', '')
            build_date = build_date.replace(',', '')
            build_date = build_date.replace('[', '')
            pitch_size = Psize.replace('\\xa0', '')
            pitch_size = pitch_size.replace(']', '')
            pitch_size = pitch_size.replace('[', '')
            pitch_size = pitch_size.replace('\'', '')
            address = add.replace('\\xa0', '')
            address = address.replace(']', '')
            address = address.replace('[', '')
            address = address.replace('\'', '')            
            label = lbl.replace('\\xa0', '')
            # temp = address
            # print("Here!")
            # print(lbl, "\n")
            # print(label, "\n\n")
            if (label != "['Record PL attendance:']"):
                print('ENTERED LOOP')
                address = pitch_size
                pitch_size = build_date
                build_date = attendance
                attendance = ""
            address = address.replace(',', ';')
            yield{

				# stadium.css('p.strong::text')[0].extract() : stadium.css('p::text')[0].extract(),
                'Name': name,
                'Address': address,
                'Capacity': capacity,
                'Pitch Size': pitch_size,
                #@tag_name --> href
                'Building Date': build_date,
                'Attendance': attendance,
                'Club': club,
            }
        