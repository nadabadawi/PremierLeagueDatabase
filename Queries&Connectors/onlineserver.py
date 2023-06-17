import datetime
# from tkinter import *
# from tkinter import ttk
# from tkcalendar import *
import mysql.connector

def Func(email, username, gender, age, club, x):
        db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
        mycursor = db.cursor()
        # if (db):
        #         print("Successful\n")
        # else: print("Failed\n")
        # x = datetime.date(2020, 5, 17)
        # print(x)
        # email = "function@gmail.com"
        # username = "trial"
        # gender = "M"
        # age = "50"
        # club = "Man Utd"

        # values = [("jello@gmail.com", "hddg", "F", x, "18", "Chelsea")]
        values = [(email, username, gender, x, age, club)]
        # print("\n\n\n")
        # print(values)
        # for i in values:
        #         for item in i:
        #                 print(type(item), "  ")
        sqlform = "INSERT INTO fan(EmailAddress,Username,Gender,BirthDate,Age,Fav_Club_Name) VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.executemany(sqlform, values)
        # result = cursor.fetchall()            # print(result)
        db.commit()

# today = datetime.date(2000, 5, 13)
# Func("moi@gmail.com", "mee", "F", "30", "Aston Villa", today)