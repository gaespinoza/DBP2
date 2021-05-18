import psycopg2

# sems = {'spring':'Spring', 'summer':'Summer','fall':'Fall','winter':'Winter'}


class Queries:
    def __init__(self):
        self.__conn = psycopg2.connect(host="localhost", port=5432, \
            dbname="gym_large", user="gaespi")
            
        self.__cur = self.__conn.cursor()
        
        self.input = -1

	#recieve user input and return the that input
    def menu_selection(self):
        self.input = input("Please Select a Number: \n" \
            "0 - Exit\n" \
            "1 - Update the Database \n" \
            "2 - View the Database \n" \
            "Input: ")
        return self.input

    #Updating Things (Add, Remove, Editing)
    def optionA(self):
        self.input = input("Please Select a Number: \n"\
            "0  - Back\n"\
            "1  - Add New League with Manager \n"\
            "2  - Update Roster and Lineup Size of League \n"\
            "3  - Create a New User \n"\
            "4  - Add a Team to a League \n"\
            "5  - Add a Gymnast to a Team \n"\
            "6  - Add a Gymnast to a Lineup \n"\
            "7  - Drop a Gymnast from a Team \n"\
            "8  - Delete a User \n"\
            "9  - Delete a Team \n"\
            "10 - Create a Gymnast \n"\
            "11 - Delete a Gymnast \n"\
            "12 - Add a New Score \n"\
            "Input: ")
        return self.input

    #Viewing Things
    def optionB(self):
        self.input = input("Please Select a Number: \n"\
            "0 - Back\n"\
            "1 - View Teams in a League \n"\
            "2 - View Teams Owned by User \n"\
            "3 - View Overall Score by a Team \n"\
            "4 - View a Team's Lineup \n"\
            "5 - View a Team's Roster \n"\
            "6 - View a User's League Membership \n"\
            "7 - View Available Gymnasts in a League \n"\
            "Input: ")
        return self.input

    def add_league(self):
        l_id = input("League ID: ")
        m_id = input("Manager ID: ")
        name = input("League Name: ")
        roster = input("Roster size: ")
        lineup = input("Lineup Size: ")

        query = "insert into league values (%s,%s,%s,%s,%s)"

        try:
            self.__cur.execute(query, (l_id, m_id,name,roster,lineup,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Addition"

    def update_ros_lin(self):
        ros_size = (input("Roster size: "))
        lin_size = (input("Lineup size: "))
        league_id = input("league id: ")

        while(lin_size>ros_size):
            print("Cannot have a smaller line up than roster size")
            ros_size = int(input("Roster size: "))
            lin_size = int(input("Lineup size: "))
        query = "update league set roster_size=%s, lineup_size=%s, where id='%s';"
        try:
            self.__cur.execute(query, (ros_size,lin_size, league_id,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Addition"

    def create_user(self):
        id = input("User id: ")
        name = input("Name: ")
        email = input("Name: ")
        password = "p@ssW0rd"

        query = "insert into users values ('%s', '%s', '%s', '%s');"

        try:
            self.__cur.execute(query, (id,name,email, password,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Addition"

    def add_team_to_league(self):
        t_id = input("Team ID: ")
        u_id = input("User ID: ")
        l_id = input("League ID: ")
        name = input("Team Name: ")
        wins = input("Wins: ")
        losses = input("Losses: ")
        query = "insert into team values (%s, %s, %s, %s, %s, %s);"

        try:
            self.__cur.execute(query, (t_id,u_id,l_id, name, wins, losses,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Addition"

    def add_gymnast_to_team(self):
        teamid = input("Team ID: ")
        gymid = input("Gymnast ID: ")

        query = "insert into roster values('%s', '%s');"
        try:
            self.__cur.execute(query, (teamid,gymid,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Addition"

    def add_gymnast_to_lineup(self):
        teamid = input("Team ID: ")
        gymid = input("Gymnast ID: ")
        event = input("Event: ")
        lineup_slot = input("Slot: ")

        query = "insert into lineup_slot values('%s', '%s', %s, '%s');"

        try:
            self.__cur.execute(query, (teamid,gymid,event,lineup_slot,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Addition"

    def drop_gymnast(self):
        teamid = input("Team ID: ")
        gymid = input("Gymnast ID: ")

        query = "delete from roster where team_id='%s' and gymnast_id='%s';"
        query1 = "delete from lineup_slot where team_id='%s' and gymnast_id='%s';"
        try:
            self.__cur.execute(query, (teamid, gymid,))
            self.__cur.execute(query1, (teamid, gymid,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Deletion"

    def delete_user(self):
        id = input("ID: ")

        query = "delete from users where id='%s"
        try:
            self.__cur.execute(query, (id,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Deletion"

    def delete_team(self):
        id = input("ID: ")

        query = "delete from team where id='%s"
        try:
            self.__cur.execute(query, (id,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Deletion"

    def create_gymnast(self):
        id = input("ID: ")
        name = input("Name: ")
        year = input("Year: ")

        query = "insert into gymnast values(%s, %s, %s)"
        try:
            self.__cur.execute(query, (id, name, year,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Entry"

    def delete_gymnast(self):
        id = input("ID: ")

        query = "delete from gymnast where id='%s"
        try:
            self.__cur.execute(query, (id,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Deletion"

    def add_score(self):
        s_id = input("Enter Score ID: ")
        g_id = input("Enter Gymnast ID: ")
        s_date = input("Enter Date of Event: ")
        event = input("Enter the Event: ")
        score = input("Enter the Score: ")
        query = "insert into score values (%s, %s, %s, %s, %s);"
        try:
            self.__cur.execute(query, (s_id, g_id, s_date, event, score,))
        except Exception as e:
            return ("Error in updating database: ", e)
        return "Successful Entry"

	#return a string that contains the advisor query
    def league_team(self):
        output = ''
        league = input("What is the league ID? \ninput: ")
        query = "select L.id as L_id, L.name as LeagueName, T.id as T_id, T.name as TeamName from league as L join team as T on L.id=T.league_id and L.id=%s;"
        self.__cur.execute(query, (league,))
        output += "Teams in League!\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "{}|".format(i.ljust(6))
        for team in self.__cur:
            output += '{}|{}|{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10), team[2].ljust(10), team[3].ljust(10))
        return output

    def user_team(self):
        output = ''
        user = input("Which User Would you like? \ninput: ")
        query = "select U.id as U_id, U.username as username, T.id as T_id, T.name as T_name from users as U join team as T on U.id=T.user_id and U.id=%s;"
        self.__cur.execute(query, (user,))
        output += f"Teams Belonging to User: {user}\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "{}|".format(i.ljust(6))
        output +="\n"
        for team in self.__cur:
            output += '{}|{}|{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10), team[2].ljust(10), team[3].ljust(10))
        return output

    def team_score(self):
        output = ''
        team = input("Which Team's Lineup do you Want to View? \ninput: ")
        query = "select Q.name, sum(S.score) from score as S join "\
            "(select T.name, T.id, R.gymnast_id from team as T "\
            "join roster as R on T.id=R.team_id where T.id=%s) "\
            "as Q on Q.gymnast_id=S.gymnast_id group by Q.name;"
        self.__cur.execute(query, (team,))
        output += f"Score for Team: {team}\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "{}|".format(i.ljust(6))
        output +="\n"
        for team in self.__cur:
            output += '{}|{}\n'.format(team[0].ljust(6), team[1].ljust(6)) 
        return output

    def team_lineup(self):
        output = ''
        team = input("Which Team's Lineup do you Want to View? \ninput: ")
        query = "select * from lineup_slot as L where L.team_id=%s;"
        self.__cur.execute(query, (team,))
        output += f"Lineup for Team: {team}\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "{}|".format(i.ljust(6))
        output +="\n"
        for team in self.__cur:
            output += '{}|{}|{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10), team[2].ljust(10), team[3].ljust(10))
        return output

    def team_roster(self):
        output = ''
        team = input("Which Team's Roster do you Want to View? \ninput: ")
        query = "select T.name, Q.team_id, Q.name, Q.year from team as T join "\
            "(select R.team_id, G.name, G.year from roster as R "\
            "join gymnast as G on R.gymnast_id = G.id and R.team_id=%s) "\
            "as Q on T.id=Q.team_id;"
        self.__cur.execute(query, (team,))
        output += f"Roster for Team: {team}\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "{}|".format(i.ljust(6))
        output +="\n"
        for team in self.__cur:
            output += '{}|{}|{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10), team[2].ljust(10), team[3].ljust(10))
        return output

    def user_league(self):
        output = ''
        user = input("Which User's League Membership do you Want to View? \ninput: ")
        query = "select U.username, Q.league_name from users as U join "\
            "(select U.user_id, L.name as league_name from user_league as U "\
            "join league as L on U.league_id = L.id where U.user_id = %s) "\
            "as Q on Q.user_id=U.id;"
        self.__cur.execute(query, (user,))
        output += f"Leagues with User: {user}\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "{}|".format(i.ljust(6))
        output +="\n"
        for team in self.__cur:
            output += '{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10))
        
        return output

    def avail_gymnasts(self):
        output = ''
        league = input("Which League would you Like to See Available Gymnasts in? \ninput: ")
        query = "select GA.id as gymnast_id, GA.name from gymnast as GA left join "\
            "(select Q.gymnast_id from team as T join "\
            "(select G.id, R.team_id, R.gymnast_id from gymnast as G join "\
            "roster as R on G.id = R.gymnast_id) "\
            "as Q on Q.team_id=T.id where T.league_id=%s) "\
            "as GU on GA.id = GU.gymnast_id where GU.gymnast_id is null;"
        self.__cur.execute(query, (league,))
        output += f"Free Gymnasts in League: {league}\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "{}|".format(i.ljust(6))
        output +="\n"
        for team in self.__cur:
            output += '{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10))
        return output

q = Queries()

while q.input != 0:
    q.menu_selection()
    if q.input == "0":
        break
    elif q.input == "1":
        q.optionA()
        if q.input == "1":
            print(q.add_league())
        elif q.input == "2":
            print(q.update_ros_lin())
        elif q.input == "3":
            print(q.create_user())
        elif q.input == "4":
            print(q.add_team_to_league())
        elif q.input == "5":
            print(q.add_gymnast_to_team())
        elif q.input == "6":
            print(q.add_gymnast_to_lineup())
        elif q.input == "7":
            print(q.drop_gymnast())
        elif q.input == "8":
            print(q.delete_user())
        elif q.input == "9":
            print(q.delete_team())
        elif q.input == "10":
            print(q.create_gymnast())
        elif q.input == "11":
            print(q.delete_gymnast())
        elif q.input == "12":
            print(q.add_score())
        elif q.input == "0":
            q.input = -1
        elif q.input > 2 or q.input < 0:
            print("Bad Input!")
    elif q.input == "2":
        q.optionB()
        if q.input == "1":
            print(q.league_team())
        elif q.input == "2":
            print(q.user_team())
        elif q.input == "3":
            print(q.team_score())
        elif q.input == '4':
            print(q.team_lineup())
        elif q.input == '5':
            print(q.team_roster())
        elif q.input == '6':
            print(q.user_league())
        elif q.input == '7':
            print(q.avail_gymnasts())
        elif q.input == "0":
            q.input = -1
        elif q.input > 3 or q.input < 0:
            print("Bad Input!")

    else:
        print("Bad Input!")
