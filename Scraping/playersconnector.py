import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "english premier league")

mycursor = mydb.cursor()

sqlform= "Insert into player(PlayerNum,Name,Nationality,DoB,Weight,Height,Position,Club2021,Club1920,Club1819,Club2122) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

file = open(r"C:\\Users\\nadab\\Spider_Projects\\players\\players\\spiders\\playwithoutloan2.csv", "r", encoding="utf8")
file_content = file.read()
content_list = file_content.split("\n")
file.close()
players = []
for i in range(1, len(content_list) - 1):
    players.append(tuple(content_list[i].split(",")))
print(players)

mycursor.executemany(sqlform, players)

mydb.commit()