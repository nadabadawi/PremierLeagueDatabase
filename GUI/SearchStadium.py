import datetime
import mysql.connector

def SearchStad(stad):
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # if (db):
    #         print("Successful\n")
    # else: print("Failed\n")
    statement = "SELECT Owning_Club_Name FROM `stadium` WHERE Name = %s"
    mycursor.execute(statement, (stad,))
    myresult = mycursor.fetchall()
    print(myresult)
    tup = myresult[0]
    # print("tup", tup)
    answer = tup[0]
    # print("answer", answer)
    return answer
    # print(len(myresult), "Here")
    # for i in range(3):
    #     print(i)
    # play_nat_list = []
    # for nat in myresult:
    #     play_nat_list.append(nat)
    # print("Here:")
    # print(play_nat_list)
    # return play_nat_list
    # for row in myresult:
    #     for attribute in row:
    #         print(attribute, "   ",)
    #     print()

# nationlist = SearchStad("Elland Road")