import datetime
import mysql.connector

def Nation():
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # if (db):
    #         print("Successful\n")
    # else: print("Failed\n")
    mycursor.execute("SELECT DISTINCT Nationality FROM `player` ORDER BY Nationality")
    myresult = mycursor.fetchall()
    # print(len(myresult), "Here")
    # for i in range(3):
    #     print(i)
    nat_list = []
    for nat in myresult:
            if (nat[0] != ''):
                nat_list.append(nat[0])
    print("\n\n", nat_list)
    return nat_list
    # for row in myresult:
    #     for attribute in row:
    #         print(attribute, "   ",)
    #     print()

nationlist = Nation()