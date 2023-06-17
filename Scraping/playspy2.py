import scrapy
import re


class Playspy2Spider(scrapy.Spider):
    name = 'playspy2'

    def start_requests(self):
        hello = open("players22.txt", "r")
        urls = []
        i = 0
        cond = True
        while cond:
            urls.append(hello.readline())
            if not urls[i]:
                cond = False
            else: 
                i = i + 1
        print("Hola")
        print(urls)
        print()
        print("Length: ", len(urls))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for play in response.css('div.playerDetails'):
            print("entered FOR LOOP")
            nm = play.css('.name::text').get()
            numb = play.css('.number::text').get()
        for player in response.css('div.col-12.u-no-padding'):
            date = player.css('.pdcol2 .info::text').get()
            if date is not None:
                date.strip()
            else:
                date = ""
            date = re.sub(r"[\n\t\s]*", "", date)
            pos = player.css('.info~ .info::text').get()
            all = player.css('span.short::text').getall()
            print("Print here: ")
            print(all)
            if (len(all) >= 4):
                s4 = all[0]
                s3 = all[1]
                s2 = all[2]
                s1 = all[3]
            elif (len(all) == 3):
                s4 = all[0]
                s3 = all[1]
                s2 = all[2]
                s1 = ""
            elif (len(all) == 2):
                s4 = all[0]
                s3 = all[1]
                s2 = ""
                s1 = ""
            elif (len(all) == 1):
                s4 = all[0]
                s3 = ""
                s2 = ""
                s1 = ""
            loan = s4.find("Loan")
            print("Before: ", s4)
            if (loan != -1):
                loan = 1
                s4 = s4.replace(' (Loan)', '')
                s4 = s4.strip()
            else:
                loan = 0
            if (nm == "Jan Bednarek"):
                s4 = "Southampton"
            yield{
				'Number': numb,
                'Name' : nm,
                'Nationality': player.css('span.playerCountry::text').get(),
                'Date of Birth': date,
                'Weight': player.css('.u-hide .info::text').extract(),            
                'Height': player.css('.pdcol3 .info::text').get(),
                'Position': pos,                
                '2020/2021': s3,
                '2019/2020': s2,
                '2018/2019': s1,
                '2021/2022' : s4
            }