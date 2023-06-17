import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "english premier league")

mycursor = mydb.cursor()

sqlform= "Insert into club(Name,Website) values(%s,%s)"

file = open(r"D:\Spring 2022\CSCE250103 - Fundmnt of database Syst\Nada Badawi - 900201364\club03ALTERED.csv", "r")
file_content = file.read()
content_list = file_content.split("\n")
file.close()
clubs = []
for i in range(1, len(content_list) - 1):
    clubs.append(tuple(content_list[i].split(",")))

mycursor.executemany(sqlform, clubs)

mydb.commit()