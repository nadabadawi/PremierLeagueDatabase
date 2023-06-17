import datetime
import mysql.connector

def Player_Pos(pos):
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # if (db):
    #         print("Successful\n")
    # else: print("Failed\n")
    statement = "SELECT Name FROM `player` WHERE Position = %s"
    mycursor.execute(statement, (pos,))
    myresult = mycursor.fetchall()
    # print("myresult", myresult)
    
    play_nat_list = []
    for nat in myresult:
        play_nat_list.append(nat[0])

    # print(play_nat_list)
    # print("Here:")
    # print(play_nat_list)
    # print("length", len(play_nat_list))
    return play_nat_list
    # for row in myresult:
    #     for attribute in row:
    #         print(attribute, "   ",)
    #     print()

# nationlist = Player_Pos("Goalkeeper")