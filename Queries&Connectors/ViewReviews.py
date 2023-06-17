import datetime
import mysql.connector

def ViewRev():
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # if (db):
    #         print("Successful\n")
    # else: print("Failed\n")
    mycursor.execute("SELECT * FROM `match_reviews_fan`")
    myresult = mycursor.fetchall()
    # print(len(myresult), "Here")
    # for i in range(3):
    #     print(i)
    return myresult
    # for row in myresult:
    #     for attribute in row:
    #         print(attribute, "   ",)
    #     print()

# reviewsTABLE = ViewRev()
# for i in range(len(reviewsTABLE)):
#     print("Here: ", reviewsTABLE[i])
#     for row in reviewsTABLE[i]:
#         print("Hello: ", row, end="  ")
#     print("End of Row")