import datetime
from tabnanny import check
import mysql.connector

def CheckFK(state, email, match_list):
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # print("\n\n\n\nSTATE:",state)
    # match_list contains date, away & home
    query1 = "SELECT COUNT(EmailAddress) FROM `fan` WHERE EmailAddress = %s GROUP BY EmailAddress;"
    query2 = "SELECT COUNT(*) FROM `match` WHERE Date = %s AND Away_Club_Name = %s AND Home_Club_Name = %s GROUP BY Date, Home_Club_Name, Away_Club_Name;"
    query1_ = "SELECT COUNT(Fan_EmailAddress) FROM `match_reviews_fan` WHERE Fan_EmailAddress = %s GROUP BY Fan_EmailAddress;"
    query2_ = "SELECT COUNT(*) FROM `match_reviews_fan` WHERE Match_Date = %s AND Away_Club_Name = %s AND Home_Club_Name = %s GROUP BY Match_Date, Home_Club_Name, Away_Club_Name;"
    if (state == 1):
        mycursor.execute(query1, (email,))
        res1 = mycursor.fetchall()
        # print("res1 when state is 1", res1)
        if len(res1) == 0:
            return True
        else:
            return False
    elif state == 2:
        mycursor.execute(query1, (email,))
        res1 = mycursor.fetchall()
        # print("\nres1 when state is 2", res1)
        mycursor.execute(query2, (match_list[0], match_list[1], match_list[2], ))
        res2 = mycursor.fetchall()
        # print("\n\nres2 when state is 2", res2)
        if (len(res1) != 0 and len(res2) != 0):
            return True
        else: return False
    elif state == 3:
        mycursor.execute(query1_, (email,))
        res1 = mycursor.fetchall()
        # print("\nres1 when state is 3", res1)
        mycursor.execute(query2_, (match_list[0], match_list[1], match_list[2], ))
        res2 = mycursor.fetchall()
        # print("\n\nres2 when state is 3", res2)
        if (len(res1) == 0 or len(res2) == 0):
            return True
        else: return False


# nationlist = WonGames(1)
# something = WonGames(2)
# Esomething = WonGames(3)
# Hsomething = WonGames(4)
# Ksomething = WonGames(5)

# dummy = ["2000-04-13", "New Crystal", "Chelsea"]
# emptyl = []
# # trial = CheckFK(2, 'nada@aucegypt.edu.com', dummy)
# # print("22trial",trial)
# # t2 = CheckFK(3, 'nada@aucegypt.edu', dummy)
# # print("22t2",t2)
# t1 = CheckFK(1, 'nada@aucegypt.edu', dummy)
# print("22t2",t1)
# te = CheckFK(1, 'nada@gmail.com', emptyl )
# print("te", te)
# #Function Input is a LIST

# # QUERY:
# SELECT COUNT(EmailAddress) FROM `fan` WHERE EmailAddress = %s GROUP BY EmailAddress;

#STATE 1: Register --> Check whether the email already exists or not to register COUNT MUST BE 0 or EMPTY VALUE
# result(quer1) == 0 or empty

#STATE 2: Review FK --> Check whether the email already exists, one condition to review COUNT MUST BE EXACTLY 1
#  ---- result(query1) == 1 && result(query2) == 1
# QUERY + ANOTHER QUERY
# ANOTHER QUERY:
# SELECT COUNT(*) FROM `match` WHERE Date = "2022-04-08" AND Away_Club_Name = "Everton" AND Home_Club_Name = "Leicester"
# GROUP BY Date, Home_Club_Name, Away_Club_Name;

#STATE 3: ADD REVIEW PK FOR TABLE REVIEW_MATCH -->Check to avoid multiple entries
# ----- result(query1) == 0 || result(query2) == 0 or empty
 



# val = ""
# list = [val] * 10
# print("It is empty:", list)
