import datetime
import mysql.connector

def FuncREV(matchDATE, homeCLUB, awayCLUB, EMAILL, textualRATE, rateNUM):
        db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
        mycursor = db.cursor()
        # if (db):
        #         print("Successful\n")
        # else: print("Failed\n")
        # x = datetime.date(2020, 5, 17)
        # print(x)
        # awayCLUB = "yesss"
        # homeCLUB = "nooo"
        # EMAILL = "50@here"
        # textualRATE = "Nic Match"
        # rateNUM = 4

        # values = [("jello@gmail.com", "hddg", "F", x, "18", "Chelsea")]
        values = [(matchDATE, awayCLUB, homeCLUB, EMAILL, textualRATE, rateNUM)]
        # print("\n\n\n")
        # print(values)
        # for i in values:
        #         for item in i:
        #                 print(type(item), "  ")
        sqlform = "INSERT INTO match_reviews_fan(Match_Date,Away_Club_Name,Home_Club_Name,Fan_EmailAddress,`Textual Rating`,Rating) VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.executemany(sqlform, values)
        # result = cursor.fetchall()            # print(result)
        db.commit()

# today = datetime.date(2000, 5, 13)
# FuncREV(today, "kdgn", "dfkgn", "lasdmf@dkfm", "this is a nice match", 4)
# FuncREV()