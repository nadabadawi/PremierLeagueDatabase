from datetime import date
import datetime
from tkinter import *
from tkinter import ttk
from turtle import pos, position
from tkcalendar import *
from PlayListByNationality import Player_Nation
from onlineserver import Func
from InsertReviews import FuncREV
from ViewReviews import ViewRev
from SearchPlayers import SearchPlay
from SearchStadium import SearchStad
from PlayerByPosition import Player_Pos
from RetrieveTeamInfo import TeamInfo
from WonMostGames import WonGames
from TeamStates import TopTen
from CheckFAN import CheckFK
from bonus import Cities

clubs = ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man Utd', 'Newcastle', 'Norwich', 'Southampton', 'Spurs', 'Watford', 'West Ham', 'Wolves']

class Notebook:
    def __init__(self):#,title):
        self.root = Tk()
        self.root.geometry("1000x1000")
        # self.root.title(title)
        self.notebook = ttk.Notebook(self.root)

    def register(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Register User") 
        instr = Label(frame, text = "Please enter the following data:")
        instr.grid(row = 0, column=0, columnspan = 2)
        em = Label(frame, text = "Email Address")
        em.grid(row = 1, column = 0)
        user = Label(frame, text = "Username")
        user.grid(row = 2, column = 0)
        gen = Label(frame, text = "Gender")
        gen.grid(row = 3, column = 0)
        birth = Label(frame, text = "Date of Birth")
        birth.grid(row = 5, column = 0, rowspan = 2)
        fav = Label(frame, text = "Favorite Club")
        fav.grid(row = 4, column = 0)
        gender_list = ['F', 'M']
        ema = Entry(frame, width = 30, borderwidth = 1)
        ema.grid(row = 1, column = 2, pady = 5)
        us = Entry(frame, width = 30, borderwidth = 1)
        us.grid(row = 2, column = 2, pady = 5)
        choice = StringVar()
        choice.set("Club")
        menu = OptionMenu(frame, choice, *clubs)
        menu.grid(row = 4, column = 2, pady = 5)
        choice2 = StringVar()
        choice2.set("Gender")
        menu2 = OptionMenu(frame, choice2, *gender_list)
        menu2.grid(row = 3, column = 2, pady = 5)
        cal = Calendar(frame, selectmode="day", year = 2000, month=1, day = 1, date_pattern = 'yyyy-MM-dd')
        cal.grid(row = 5, column = 2, rowspan = 2, pady = 5)
        dob = Label(frame, text = "")
        button = Button(frame, text = "Choose Date", command = lambda: self.GetDate(cal = cal, dob = dob))
        button.grid(row = 5, column = 3, padx = 10)
        dob.grid(row = 6, column = 3)
        def error2():
            errormessage = Label(frame, text = "Make sure you have chosen the correct date of birth. Dates past 2021 are not allowed")
            errormessage.grid(row = 7, column = 2, padx = 5)
            frame.after(5000, lambda: errormessage.configure(text = ""))
            frame.after(5000, lambda: dob.config(text = ""))
        def problemo():
            errormessage = Label(frame, text = "User Email Address Already Registered!")
            errormessage.grid(row = 7, column = 2, padx = 5)
            frame.after(5000, lambda: errormessage.configure(text = ""))
        def data():
            # vals = []
            email = ema.get()
            username = us.get()
            gender = choice2.get()
            birthdate = dob.cget("text")
            club = choice.get()
            byear = birthdate[0:4]
            bmonth = birthdate[5:7]
            bday = birthdate[8:10]
            empty_list = []
            if (int(byear) > 2021):
                error2()
            else:
                dte = datetime.date(int(byear), int(bmonth), int(bday))
                age = int(date.today().year) - int(byear)
                age_str = str(age)
                # vals = [(email, username, gender, dte, age_str, club)]
                if (CheckFK(1, email, empty_list)):
                    Func(email, username, gender, age_str, club, dte)
                    self.refresh(ema, us, choice2, dob, choice)
                else:
                    problemo()
            # return vals

        sub = Button(frame, text = "Submit", command = data)
        sub.grid(row = 7, column = 1)
        
        
        self.notebook.pack()

    def GetDate(self, cal, dob):
            dt = cal.get_date()
            dob.config(text = dt)
    
    def review(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Add Review")

        can1 = Canvas(frame)
        can1.pack(side = 'left', fill ="both", expand = 1)
        scroll1 = ttk.Scrollbar(frame, orient = "vertical", command = can1.yview)
        scroll1.pack(side = "right", fill = 'y')

        can1.configure(yscrollcommand = scroll1.set)
        can1.bind('<Configure>', lambda e: can1.configure(scrollregion = can1.bbox("all")))

        tab2 = Frame(can1)
        can1.create_window((0,0), window = tab2, anchor = "nw")

        def error1():
            errormessage = Label(tab2, text = "Incorrect date given. Please choose the correct date")
            errormessage.grid(row = 8, column = 2, padx = 5, columnspan = 7)
            tab2.after(3000, lambda: errormessage.configure(text = ""))
            tab2.after(3000, lambda: Mdate.config(text = ""))

        def reset():
            Mdate.config(text = "")
            homeChoice.set("Home Team")
            awayChoice.set("Away Team")
            Email_.delete(0, 'end')
            TextRate.delete('1.0', END)
            rating.set("0")

        def Review():
            matchDATEtemp = Mdate.cget("text")
            homeCLUB = homeChoice.get()
            awayCLUB = awayChoice.get()
            EMAILl = Email_.get()
            textualRATE = TextRate.get(1.0, END)
            rateNUM = rating.get()
            myear = matchDATEtemp[0:4]
            mmonth = matchDATEtemp[5:7]
            mday = matchDATEtemp[8:10]
            def problemo(textt):
                errormessage = Label(tab2, text = textt)
                errormessage.grid(row = 8, column = 2, padx = 5, columnspan= 7)
                frame.after(5000, lambda: errormessage.configure(text = ""))
            if (int(myear) > 2022 or int(myear) < 2018):
                error1()
            else:
                
                matchDATE = datetime.date(int(myear), int(mmonth), int(mday))
                mat_list = [matchDATE, awayCLUB, homeCLUB]
                print("\n\n\nHeree",CheckFK(2, EMAILl, mat_list))
                if not CheckFK(2, EMAILl, mat_list):
                    problemo("Incorrect Data Entered: Invalid Match Details OR Non-registered Email Address")
                elif not CheckFK(3, EMAILl, mat_list):
                    problemo("You already reviewed this match. (Try reviewing a different match or change Email Address)")
                else:
                    FuncREV(matchDATE, homeCLUB, awayCLUB, EMAILl, textualRATE, rateNUM)
                    reset()


        instr = Label(tab2, text = "Please enter the following data:")
        instr.grid(row = 0, column=0, columnspan = 2)
        match_date = Label(tab2, text = "Match Date")
        match_date.grid(row = 1, column = 0)
        home_club = Label(tab2, text = "Home Club")
        home_club.grid(row = 3, column = 0)
        away_club = Label(tab2, text = "Away Club")
        away_club.grid(row = 4, column = 0)
        fan_email = Label(tab2, text = "Email Address")
        fan_email.grid(row = 5, column = 0)
        textual = Label(tab2, text = "Rating (Text)")
        textual.grid(row = 6, column = 0)
        rate = Label(tab2, text = "Rate")
        rate.grid(row = 7, column = 0)

        def GetDate2():
            tare5 = cal2.get_date()
            Mdate.config(text = tare5)

        cal2 = Calendar(tab2, selectmode="day", year = 2018, month=8, day = 1, date_pattern = 'yyyy-MM-dd')
        cal2.grid(row = 1, column = 2, rowspan = 2, columnspan = 5, pady = 5)
        Mdate = Label(tab2, text = "")
        button2 = Button(tab2, text = "Choose Date", command = GetDate2)
        button2.grid(row = 1, column = 7, padx = 10)
        Mdate.grid(row = 2, column = 7, pady = 5)

        homeChoice = StringVar()
        homeChoice.set("Home Team")
        homeMenu = OptionMenu(tab2, homeChoice, *clubs)
        homeMenu.grid(row = 3, column = 2, columnspan = 5, pady = 5)

        awayChoice = StringVar()
        awayChoice.set("Away Team")
        awayMenu = OptionMenu(tab2, awayChoice, *clubs)
        awayMenu.grid(row = 4, column = 2, columnspan = 5, pady = 5)


        Email_ = Entry(tab2, width = 40, borderwidth = 1)
        Email_.grid(row = 5, column = 2, columnspan = 5, pady = 5)
        TextRate = Text(tab2, width = 30, borderwidth = 1)
        TextRate.grid(row = 6, column = 2, columnspan = 5, pady = 5)
        rating = IntVar()
        Radiobutton(tab2, text = "1", variable=rating, value = 1).grid(row = 7, column = 2, pady = 5)
        Radiobutton(tab2, text = "2", variable=rating, value = 2).grid(row = 7, column = 3, pady = 5)
        Radiobutton(tab2, text = "3", variable=rating, value = 3).grid(row = 7, column = 4, pady = 5)
        Radiobutton(tab2, text = "4", variable=rating, value = 4).grid(row = 7, column = 5, pady = 5)
        Radiobutton(tab2, text = "5", variable=rating, value = 5).grid(row = 7, column = 6, pady = 5)

        subm = Button(tab2, text = "Submit", command = Review)
        subm.grid(row = 8, column = 1, pady = 5)

        scrollbar = Scrollbar(tab2, orient = 'vertical', command = TextRate.yview)
        scrollbar.grid(row = 6, column = 7, sticky = 'ns')
        TextRate['yscrollcommand'] = scrollbar.set
        self.notebook.pack()

    def viewreview(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="View Match Reviews")
        canvas2 = Canvas(frame)
        canvas2.pack(side = 'left', fill ="both", expand = 1)
        scrollbar_2 = ttk.Scrollbar(frame, orient = "vertical", command = canvas2.yview)
        scrollbar_2.pack(side = "right", fill = 'y')

        canvas2.configure(yscrollcommand = scrollbar_2.set)
        canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion = canvas2.bbox("all")))

        tab3 = Frame(canvas2)
        canvas2.create_window((0,0), window = tab3, anchor = "nw")

        def ref3(index, text):
            tab3.after(50, lambda: all_reviews[index].configure(text=text))
        def wer3(event):
            reviewsTABLE = ViewRev()
            t = len(reviewsTABLE)
            for s in range(0, 100):
                for l in range(6):
                    ref3(l + 6*(s), "")
            # print("LIst:", play_nat_list)
            k = 0
            counter = 0
            # print("t", t)
            while (k < t):
                j = 0
                item = reviewsTABLE[k]
                # print("Item:", item)
                while (j < 6):
                    # print(k, j)
                    element = item[j]
                    # print(element)
                    counter = j + 6*(k)
                    # print("counter", counter)
                    ref3(counter,element)
                    j = j + 1
                k = k + 1

        self.notebook.bind('<<NotebookTabChanged>>', wer3)
        match_date2 = Label(tab3, text = "Match Date")
        match_date2.grid(row = 0, column = 1, pady = 5, padx = 5)
        home_club2 = Label(tab3, text = "Home Club")
        home_club2.grid(row = 0, column = 2, pady = 5, padx = 5)
        away_club2 = Label(tab3, text = "Away Club")
        away_club2.grid(row = 0, column = 3, pady = 5, padx = 5)
        fan_email2 = Label(tab3, text = "Email Address")
        fan_email2.grid(row = 0, column = 4, pady = 5, padx = 5)
        textual2 = Label(tab3, text = "Rating (Text)")
        textual2.grid(row = 0, column = 5, pady = 5, padx = 5)
        rate2 = Label(tab3, text = "Rate")
        rate2.grid(row = 0, column = 6, pady = 5, padx = 5)

        all_reviews = []
        for i in range(100):
            col = 0
            for j in range(6):
                looplabel5 = Label(tab3, text = "")
                all_reviews.append(looplabel5)
                looplabel5.grid(row = i + 1, column = col, pady = 5, padx = 5)
                col = col + 1

        self.notebook.pack()
    
    def nationality(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Search by Player's Nationality")
        nationalities = ['Albania', 'Algeria', 'Argentina', 'Austria', 'Belgium', 'Bosnia & Herzegovina', 'Brazil', 'Burkina Faso', 'Cameroon', 'Chile', 'Colombia', 'Cote D’Ivoire', 'Croatia', 'Czech Republic', 'Denmark', 'DR Congo', 'Ecuador', 'Egypt', 'England', 'Estonia', 'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guinea', 'Iceland', 'Iran', 'Iraq', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Kosovo', 'Mali', 'Mexico', 'Montenegro', 'Morocco', 'Netherlands', 'New Zealand', 'Nigeria', 'Northern Ireland', 'Norway', 'Paraguay', 'Poland', 'Portugal', 'Romania', 'Scotland', 'Senegal', 'Serbia', 'Slovakia', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Tunisia', 'Turkey', 'Ukraine', 'United States', 'Uruguay', 'Venezuela', 'Wales', 'Zambia', 'Zimbabwe']

        canvas = Canvas(frame)
        canvas.pack(side = 'left', fill ="both", expand = 1)
        scrollbar_ = ttk.Scrollbar(frame, orient = "vertical", command = canvas.yview)
        scrollbar_.pack(side = "right", fill = 'y')

        canvas.configure(yscrollcommand = scrollbar_.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

        second_frame = Frame(canvas)
        canvas.create_window((0,0), window = second_frame, anchor = "nw")

        # nation_Label = Label(second_frame, text = "Nationality")
        # nation_Label.grid(row = 0, column = 0, padx = 50)
        play_name = Label(second_frame, text = "Player Name")
        play_name.grid(row = 1, column = 0, padx = 50)
        Season = Label(second_frame, text = "Season")
        Season.grid(row = 1, column = 1)
        c21 = Label(second_frame, text = "2021/22")
        c21.grid(row = 1, column = 2, padx = 50)
        c20 = Label(second_frame, text = "2020/21")
        c20.grid(row = 1, column = 3, padx = 50)
        c19 = Label(second_frame, text = "2019/20")
        c19.grid(row = 1, column = 4, padx = 50)
        c18 = Label(second_frame, text = "2018/19")
        c18.grid(row = 1, column = 5, padx = 50)
        var = 0
        def ref(index, text):
            second_frame.after(50, lambda: all_entries[index].configure(text=text))
        def wer(event):
            play_nat_list = Player_Nation(clicked.get())
            t = len(play_nat_list)
            var = t
            
            for s in range(0, 600):
                for l in range(5):
                    ref(l + 5*(s), "")
            k = 0
            counter = 0
            while (k < t):
                j = 0
                item = play_nat_list[k]
                while (j < 5):
                    element = item[j]
                    counter = j + 5*(k)
                    ref(counter,element)
                    j = j+1
                k = k + 1


        clicked = StringVar()
        clicked.set("Nationality")
        drop = OptionMenu(second_frame, clicked, *nationalities, command = wer)
        drop.grid(row = 0, column = 1, padx = 75, columnspan = 5, ipadx = 100)

        all_entries = []
        for i in range(600):
            col = 0
            for j in range(5):
                looplabel3 = Label(second_frame, text = "")
                all_entries.append(looplabel3)
                looplabel3.grid(row = i + 2, column = col, pady = 5, padx = 5)
                if (col == 0):
                    col = col + 2
                else:
                    col = col + 1

        self.notebook.pack()

    def playerbyname(self):
        playerinfoFrame = ttk.Frame(self.notebook)
        self.notebook.add(playerinfoFrame,text="Search by Player's Name")

        def Clear_First(event):
            firstLab.delete(0, 'end')
        def Clear_Sec(event):
            secLab.delete(0, 'end')

        def error():
            errormessage = Label(playerinfoFrame, text = "There is no match to the given data. Please try again.")
            errormessage.grid(row = 4, column = 4, padx = 5)
            playerinfoFrame.after(5000, lambda: errormessage.configure(text = ""))


        firstLab = Entry(playerinfoFrame, width = 50)
        firstLab.bind("<Button-1>", Clear_First)
        firstLab.grid(row = 0, column = 0, pady = 50, padx = 50, columnspan = 5)
        firstLab.insert(0, "Enter First Name Here")
        secLab = Entry(playerinfoFrame, width = 50)
        secLab.bind("<Button-1>", Clear_Sec)
        secLab.grid(row = 0, column = 5, pady = 50, padx = 20, columnspan = 5)
        secLab.insert(0, "Enter Last Name Here")
        my_players = []
        for i in range(2):
                col = 0
                for j in range(11):
                    looplabel4 = Label(playerinfoFrame, text = "")
                    my_players.append(looplabel4)
                    looplabel4.grid(row = i + 2, column = col, pady = 5, padx = 5)
                    col = col + 1
        # print("length:", len(my_players), "my_players", my_players)

        numLab = Label(playerinfoFrame, text = "Number")
        numLab.grid(row = 1, column = 0)
        name_Lab = Label(playerinfoFrame, text = "Name")
        name_Lab.grid(row = 1, column = 1)
        nation_lab = Label(playerinfoFrame, text = "Nationality")
        nation_lab.grid(row = 1, column = 2)
        doblab = Label(playerinfoFrame, text = "Birth Date")
        doblab.grid(row = 1, column = 3)
        weight = Label(playerinfoFrame, text = "Weight")
        weight.grid(row = 1, column = 4)
        height = Label(playerinfoFrame, text = "Height")
        height.grid(row = 1, column = 5)
        posit_lab = Label(playerinfoFrame, text = "Position")
        posit_lab.grid(row = 1, column = 6)
        c20lab = Label(playerinfoFrame, text = "2020/21")
        c20lab.grid(row = 1, column = 7)
        c19lab = Label(playerinfoFrame, text = "2019/20")
        c19lab.grid(row = 1, column = 8)
        c18lab = Label(playerinfoFrame, text = "2018/19")
        c18lab.grid(row = 1, column = 9)
        c21lab = Label(playerinfoFrame, text = "2021/22")
        c21lab.grid(row = 1, column = 10)



        def ref2(index, text):
            playerinfoFrame.after(50, lambda: my_players[index].configure(text=text))
        def wer2():
            fullName = firstLab.get() + " " + secLab.get()
            playersinfo_list = SearchPlay(fullName)
            num = len(playersinfo_list)
            if num == 0:
                error()
            print("FullName", fullName)
            t = len(playersinfo_list)
            print("List: ",playersinfo_list)
            print("size: ",t)
            for s in range(0, 2):
                for l in range (11):
                    ref2(l + 11*(s), "")
            k = 0
            counter = 0
            while (k < t):
                j = 0
                item = playersinfo_list[k]
                # print("Item:", item)
                while (j < 11):
                    element = item[j]
                    # print(element)
                    counter = j + 11*(k)
                    # print("counter", counter)
                    ref2(counter,element)
                    j = j+1
                k = k + 1
            
        search_button = Button(playerinfoFrame, text = "Search", command =  wer2)
        search_button.grid(row = 0, column = 10)


        self.notebook.pack()

    def stadium(self):
        stadinfoFrame = ttk.Frame(self.notebook)
        self.notebook.add(stadinfoFrame,text="Search for a Club by Stadium Name")
        stadium_list = ['Amex Stadium', 'Brentford Community Stadium', 'Carrow Road Stadium Map', 'Elland Road', 'Emirates Stadium', 'Etihad Stadium Map', 'Goodison Park Stadium Map', 'King Power Stadium Map', 'London Stadium Map', 'Molineux Stadium', 'Old Trafford Stadium Map', 'Selhurst Park Stadium Map', 'St Marys Stadium Map', "St. James' Park", 'Stadium Map', 'Stamford Bridge Stadium Map', 'Tottenham Hotspur Stadium', 'Turf Moor Stadium Map', 'Vicarage Road Stadium Map', 'Villa Park Stadium Map']
        def SearchStadium(event):
            stadinfoFrame.after(50, lambda: HTeamLab.configure(text=SearchStad(click.get())))

        click = StringVar()
        click.set("Choose a Stadium to know its Owning Club")
        drop2 = OptionMenu(stadinfoFrame, click, *stadium_list, command = SearchStadium)
        drop2.grid(row = 0, column = 0)

        TagHTeam = Label(stadinfoFrame, text = "Owning Club Name: ")
        TagHTeam.grid(row = 0, column = 1)
        print("DropDown Menu: ", click.get())
        # HTeam = SearchStad(click.get())
        # print("HTEAM: ", HTeam)
        HTeamLab = Label(stadinfoFrame, text = "")
        HTeamLab.grid(row = 0, column = 2)

        self.notebook.pack()    

    def playerbyposition(self):
        positionFrame = ttk.Frame(self.notebook)
        self.notebook.add(positionFrame,text="Search by Player's Position")

        positions = ['Goalkeeper', 'Midfielder', 'Forward', 'Defender']
        canvas3 = Canvas(positionFrame)
        canvas3.pack(side = 'left', fill ="both", expand = 1)
        scrollbar_3 = ttk.Scrollbar(positionFrame, orient = "vertical", command = canvas3.yview)
        scrollbar_3.pack(side = "right", fill = 'y')

        canvas3.configure(yscrollcommand = scrollbar_3.set)
        canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion = canvas3.bbox("all")))
        second_frame2 = Frame(canvas3)
        canvas3.create_window((0,0), window = second_frame2, anchor = "nw")

        def ref4(index, text):
            second_frame2.after(50, lambda: my_pos_labels[index].configure(text=text))
        def ind(index, text):
            second_frame2.after(50, lambda: indices2[index].configure(text=text))
        def wer4(event):
            pos_list = Player_Pos(cl.get())
            t = len(pos_list)
            for s in range(0, 400):
                ref4(s, "")
                ind(s, "")
            k = 0
            counter = 0
            while (k < t):    
                item = pos_list[k]
                ref4(k, item)
                ind(k, str(k+1))
                k = k + 1

        cl = StringVar()
        cl.set("Choose a Position")
        drop3 = OptionMenu(second_frame2, cl, *positions, command = wer4)
        drop3.grid(row = 0, column = 0)

        my_pos_labels = []
        indices2 = []
        for i in range(400):
            labindex2 = Label(second_frame2, text = "")
            indices2.append(labindex2)
            labindex2.grid(row = i + 1, column = 0, pady = 5, padx = 5)
            looplabel6 = Label(second_frame2, text = "")
            my_pos_labels.append(looplabel6)
            looplabel6.grid(row = i + 1, column = 1, pady = 5, padx = 5)

        self.notebook.pack()
    
    def teaminfo(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Team Info")
        team = Label(frame, text = "Team")
        team.grid(row = 1, column = 0, padx = 50)
        website = Label(frame, text = "Website")
        website.grid(row = 1, column = 1, padx = 50)

        def ref6(index, text):
            frame.after(50, lambda: all_entries[index].configure(text=text))
        def wer6(event):
            list_team = TeamInfo(clicked.get())
            print("LIST",list_team)
            t = len(list_team)
            # var = t
            print("t", t)
            for l in range(0, 2):
                # for l in range(5):
                ref6(l, "")
            # k = 0
            # counter = 0
            # while (k < t):
                j = 0
                # item = list_team[k]
                while (j < 2):
                    element = list_team[j]
                    # counter = j + 5*(k)
                    ref6(j,element)
                    j = j + 1
                # k = k + 1
        clicked = StringVar()
        clicked.set("Choose a Team")
        drop = OptionMenu(frame, clicked, *clubs, command = wer6)
        drop.grid(row = 0, column = 1, padx = 75, columnspan = 5, ipadx = 100)

        all_entries = []
        # for i in range(600):
        #     col = 0
        for j in range(2):
            looplabel3 = Label(frame, text = "")
            all_entries.append(looplabel3)
            looplabel3.grid(row = 2, column = j, pady = 5, padx = 5)
            # if (col == 0):
            #     col = col + 2
            # else:
            #     col = col + 1

        self.notebook.pack()

    def TopTeam(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Season Top Team")
        season = Label(frame, text = "Season")
        season.grid(row = 0, column = 0, padx = 50)
        team = Label(frame, text = "Team")
        team.grid(row = 0, column = 1, padx = 50)

        text4 = WonGames(4)
        text3 = WonGames(3)
        text2 = WonGames(2)
        text1 = WonGames(1)

        s1 = Label(frame, text = "2021/22")
        s1.grid(row = 1, column = 0, padx = 50)
        s2 = Label(frame, text = "2020/21")
        s2.grid(row = 2, column = 0, padx = 50)
        s3 = Label(frame, text = "2019/20")
        s3.grid(row = 3, column = 0, padx = 50)
        s4 = Label(frame, text = "2018/19")
        s4.grid(row = 4, column = 0, padx = 50)
        a1 = Label(frame, text = text4)
        a1.grid(row = 1, column = 1, padx = 50)
        a2 = Label(frame, text = text3)
        a2.grid(row = 2, column = 1, padx = 50)
        a3 = Label(frame, text = text2)
        a3.grid(row = 3, column = 1, padx = 50)
        a4 = Label(frame, text = text1)
        a4.grid(row = 4, column = 1, padx = 50)
        
    def toptenteams(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Top Ten Teams")
        lab = Label(frame, text = "Show Top 10 Teams By:")
        lab.grid(row = 0, column = 0, padx = 50)

        states = ["Matches Won", "Home Matches Won", "Yellow Cards", "Fouls", "Shots"]

        def ref7(index, text):
            frame.after(50, lambda: all_entries[index].configure(text=text))
        def wer7(event):
            chosen = clicked.get()
            if chosen == "Matches Won":
                list_team = TopTen(1)
            elif chosen == 'Home Matches Won':
                list_team = TopTen(2)
            elif chosen == "Yellow Cards":
                list_team = TopTen(3)
            elif chosen == "Fouls":
                list_team = TopTen(4)
            elif chosen == "Shots":
                list_team = TopTen(5)
                
            print("LIST",list_team)
            t = len(list_team)
            # var = t
            print("t", t)

            for s in range(0, 10):
                # for l in range(5):
                ref7(s, "")
            k = 0
            counter = 0
            while (k < t):
                # j = 0
                item = list_team[k]
                ref7(k,item)
                k = k + 1

        all_entries = []
        for i in range(10):
            labelindex = Label(frame, text = i + 1)
            labelindex.grid(row = i + 1, column = 0)
            looplabel3 = Label(frame, text = "")
            all_entries.append(looplabel3)
            looplabel3.grid(row = i + 1, column = 1, pady = 5, padx = 5)            

        clicked = StringVar()
        clicked.set("")
        drop = OptionMenu(frame, clicked, *states, command = wer7)
        drop.grid(row = 0, column = 1, padx = 75, columnspan = 5, ipadx = 100)

    def bonus(self):
        bonusFrame = ttk.Frame(self.notebook)
        self.notebook.add(bonusFrame,text="Search Team by City")

        cities = ['London', 'Lancashire', 'Brighton', 'Brentford', 'Liverpool', 'Birmingham', 'Leeds', 'Leicester', 'Manchester', 'Southampton', 'Norwich', 'Newcastle Upon Tyne', 'Hertfordshire', 'Wolverhampton']
        cities.sort()
        # print(cities)
        def ref5(index, text):
            bonusFrame.after(50, lambda: my_clubs_labels[index].configure(text=text))
        def ind1(index, text):
            bonusFrame.after(50, lambda: indices3[index].configure(text=text))
        def wer5(event):
            clubb_list = Cities(ch.get())
            t = len(clubb_list)
            for s in range(10):
                ref5(s, "")
                ind1(s, "")
            k = 0
            while (k < t):    
                item = clubb_list[k]
                ref5(k, item)
                ind1(k, str(k+1))
                k = k + 1
        ch = StringVar()
        ch.set("Choose a City to know the Teams in it")
        drop2 = OptionMenu(bonusFrame, ch, *cities, command = wer5)
        drop2.grid(row = 0, column = 0)
        hclubs = Label(bonusFrame, text = "Clubs: ")
        hclubs.grid(row = 1, column = 0)
        my_clubs_labels = []
        indices3 = []
        for i in range(10):
            labindex3 = Label(bonusFrame, text = "")
            indices3.append(labindex3)
            labindex3.grid(row = i + 2, column = 0, pady = 5, padx = 5)
            looplabel7 = Label(bonusFrame, text = "")
            my_clubs_labels.append(looplabel7)
            looplabel7.grid(row = i + 2, column = 1, pady = 5, padx = 5)

        self.notebook.pack()

    def exit(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Exit")    
        exitButton = Button(frame, text = "Exit", command = self.root.quit, width = 20, height = 5)
        exitButton.pack(pady = 100)
        self.notebook.pack()

    def refresh(self, ema, us, choice2, dob, choice):
        ema.delete(0, 'end')
        us.delete(0, 'end')
        choice2.set("Gender")
        dob.config(text="")
        choice.set("Club")

# if (int(myear) > 2022 or int(myear) < 2018):
#                 error1()
#             else:
#                 matchDATE = datetime.date(int(myear), int(mmonth), int(mday))
#                 FuncREV(matchDATE, homeCLUB, awayCLUB, EMAILL, textualRATE, rateNUM)


    def run(self):
        self.root.mainloop()

nb = Notebook()
nb.register()
nb.review()
nb.viewreview()
nb.nationality()
nb.playerbyname()
nb.stadium()
nb.playerbyposition()
nb.bonus()
nb.teaminfo()
nb.TopTeam()
nb.toptenteams()
nb.exit()
nb.run()

# root.mainloop()
