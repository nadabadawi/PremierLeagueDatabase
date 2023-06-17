import datetime
import mysql.connector

def WonGames(season):
    db = mysql.connector.connect(host = "db4free.net", user = "", password = "", database = "epleague")
    mycursor = db.cursor()
    # if (db):
    #         print("Successful\n")
    # else: print("Failed\n")
    # Show all the teams who won the most games by season
    # SELECT DISTINCT (won clubs)
    # SELECT  team from (
    # SELECT DISTINCT team, COUNT(DISTINCT team)) as matches from (
    # SELECT HomeTeam as team where home goals > away_goals AND season = season # home clubs that won the match
    # UNION
    # SELECT Awayteam as team where away goals > home_goals # away clubs that won the match
    # )
    # ) order by desc limit 1
    statement = "SELECT Team FROM ( SELECT Home_Club_Name AS Team FROM `match` where Home_Goals > Away_Goals AND Season = %s UNION ALL SELECT Away_Club_Name AS Team FROM `match` where Away_Goals > Home_Goals AND Season = %s ) AS R1 GROUP BY Team ORDER BY COUNT(Team) DESC LIMIT 1;"
    # statement = "SELECT Owning_Club_Name FROM `stadium` WHERE Name = %s"
    mycursor.execute(statement, (season,season, ))
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        print("It is empty:")
        return ""
    else:
        print("mys result: ",myresult)
        tup = myresult[0]
        element = tup[0]
        print("tup", tup)
        print("Element: ", element)
        return element

nationlist = WonGames(3)