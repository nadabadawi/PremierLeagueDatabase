import datetime
import mysql.connector

def TopTen(state):
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    print("\n\n\n\nSTATE:",state)
    

    if (state == 1):
        statement = "SELECT Team FROM ( SELECT Home_Club_Name AS Team FROM `match` where Home_Goals > Away_Goals UNION ALL SELECT Away_Club_Name AS Team FROM `match` where Away_Goals > Home_Goals) AS R1 GROUP BY Team ORDER BY COUNT(Team) DESC LIMIT 10;"
    elif state == 2:
        statement = "SELECT Home_Club_Name AS Team FROM `match` where Home_Goals > Away_Goals GROUP BY Home_Club_Name ORDER BY COUNT(Home_Club_Name) DESC LIMIT 10;"
    elif state == 3:
        statement = "SELECT Team FROM ( SELECT Home_Club_Name AS Team, SUM(Home_YellowCard) AS YC FROM `match` GROUP BY Home_Club_Name Union SELECT Away_Club_Name AS Team, SUM(Away_YellowCard) AS YC FROM `match` GROUP BY Away_Club_Name ) AS Res2 GROUP BY Team ORDER BY SUM(YC) DESC LIMIT 10;"
    elif state == 4:
        statement = "SELECT Team FROM ( SELECT Home_Club_Name AS Team, SUM(Home_Fouls) AS YC FROM `match` GROUP BY Home_Club_Name Union SELECT Away_Club_Name AS Team, SUM(Away_Fouls) AS YC FROM `match` GROUP BY Away_Club_Name ) AS Res3 GROUP BY Team ORDER BY SUM(YC) DESC LIMIT 10;"
    elif state == 5:
        statement = "SELECT Team FROM ( SELECT Home_Club_Name AS Team, SUM(Home_Shots) AS YC FROM `match` GROUP BY Home_Club_Name Union SELECT Away_Club_Name AS Team, SUM(Away_Shots) AS YC FROM `match` GROUP BY Away_Club_Name ) AS Res4 GROUP BY Team ORDER BY SUM(YC) DESC LIMIT 10;"


    # statement = "SELECT Team FROM (SELECT Home_Club_Name AS Team FROM `match` where Home_Goals > Away_Goals AND Season = %s UNION ALL SELECT Away_Club_Name AS Team FROM `match` where Away_Goals > Home_Goals AND Season = %s ) AS R1 GROUP BY Team ORDER BY COUNT(Team) DESC LIMIT 1;"
    # statement = "SELECT Owning_Club_Name FROM `stadium` WHERE Name = %s"
    mycursor.execute(statement)
    myresult = mycursor.fetchall()
    final_list = []
    val = ""
    list = [val] * 10
    if len(myresult) == 0:
        print("It is empty:", list)
        return list
    else:
        for tuple in myresult:
            final_list.append(tuple[0])
        print("my result: ", myresult)
        print("final_list:", final_list)
        return final_list

# nationlist = WonGames(1)
# something = WonGames(2)
# Esomething = WonGames(3)
# Hsomething = WonGames(4)
# Ksomething = WonGames(5)

# matches won, home matches won

#STATE 1
# SELECT Team FROM ( SELECT Home_Club_Name AS Team FROM `match` where Home_Goals > Away_Goals
# UNION ALL SELECT Away_Club_Name AS Team FROM `match` where Away_Goals > Home_Goals)
# AS R1 GROUP BY Team ORDER BY COUNT(Team) DESC LIMIT 10;

#STATE 2
# SELECT Home_Club_Name AS Team FROM `match` where Home_Goals > Away_Goals
# GROUP BY Home_Club_Name ORDER BY COUNT(Home_Club_Name) DESC LIMIT 10;

#STATE 3
#SELECT Team, SUM(YC) FROM ( SELECT Home_Club_Name AS Team, SUM(Home_YellowCard) AS YC FROM `match` GROUP BY Home_Club_Name Union SELECT Away_Club_Name AS Team, SUM(Away_YellowCard) AS YC FROM `match` GROUP BY Away_Club_Name ) AS Res2 GROUP BY Team ORDER BY SUM(YC) DESC LIMIT 10;

#STATE 4
# SELECT Team, SUM(YC) FROM ( SELECT Home_Club_Name AS Team, SUM(Home_Fouls) AS YC FROM `match` GROUP BY Home_Club_Name Union SELECT Away_Club_Name AS Team, SUM(Away_Fouls) AS YC FROM `match` GROUP BY Away_Club_Name ) AS Res3 GROUP BY Team ORDER BY SUM(YC) DESC LIMIT 10;


#STATE 5
# SELECT Team, SUM(YC) FROM ( SELECT Home_Club_Name AS Team, SUM(Home_Shots) AS YC FROM `match` GROUP BY Home_Club_Name Union SELECT Away_Club_Name AS Team, SUM(Away_Shots) AS YC FROM `match` GROUP BY Away_Club_Name ) AS Res4 GROUP BY Team ORDER BY SUM(YC) DESC LIMIT 10;

# val = ""
# list = [val] * 10
# print("It is empty:", list)
