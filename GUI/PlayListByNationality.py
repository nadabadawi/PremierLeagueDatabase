import datetime
import mysql.connector

def Player_Nation(national):
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # if (db):
    #         print("Successful\n")
    # else: print("Failed\n")
    statement = "SELECT Name, Club2122, Club2021, Club1920, Club1819 FROM `player` WHERE Nationality = %s"
    mycursor.execute(statement, (national,))
    myresult = mycursor.fetchall()
    # print(len(myresult), "Here")
    # for i in range(3):
    #     print(i)
    play_nat_list = []
    for nat in myresult:
        play_nat_list.append(nat)
    # print("Here:")
    # print(play_nat_list)
    return play_nat_list
    # for row in myresult:
    #     for attribute in row:
    #         print(attribute, "   ",)
    #     print()

# nationlist = Player_Nation("Egypt")