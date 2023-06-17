import datetime
import mysql.connector

def SearchPlay(name):
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # if (db):
    #         print("Successful\n")
    # else: print("Failed\n")
    statement = "SELECT * FROM `player` WHERE Name = %s"
    mycursor.execute(statement, (name,))
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

nationlist = SearchPlay("Mohamed Elneny")