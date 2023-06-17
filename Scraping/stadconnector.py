import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "english premier league")

mycursor = mydb.cursor()

sqlform= "Insert into stadium(Name,Address,Capacity,PitchSize,BuildingDate,LeagueAttendance,Owning_Club_Name) values(%s,%s,%s,%s,%s,%s,%s)"

file = open(r"C:\\Users\\nadab\\Spider_Projects\\players\\players\\spiders\\stadiumFINAL1.csv", "r", encoding="utf8")
file_content = file.read()
content_list = file_content.split("\n")
file.close()
stadiums = []
for i in range(1, len(content_list) - 1):
    stadiums.append(tuple(content_list[i].split(",")))

mycursor.executemany(sqlform, stadiums)

mydb.commit()