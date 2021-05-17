import psycopg2

# sems = {'spring':'Spring', 'summer':'Summer','fall':'Fall','winter':'Winter'}


class Queries:
    def __init__(self):
        self.__conn = psycopg2.connect(host="localhost", port=5432, \
            dbname="big_b", user="gaespi")
            
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
            "0 - Back\n"\
            "1 - Add New League with Manager \n"\
            "2 - Create a New User \n"\
            "Input: ")
        return self.input

    #Viewing Things
    def optionB(self):
        self.input = input("Please Select a Number: \n"\
            "0 - Back\n"\
            "1 - View Teams in a League \n"\
            "2 - View Teams Owned by User \n"\
            "3 - View Overall Score by a Team \n"\
            "Input: ")
        return self.input

	#return a string that contains the advisor query
    def league_team(self):
        output = ''
        league = input("What is the league ID? \ninput: ")
        query = "select L.id as L_id, L.name as LeagueName, T.id as T_id, T.name as TeamName from league as L join team as T on L.id=T.league_id and L.id=%s;"
        self.__cur.execute(query, (league,))
        output += "Teams in League!\n"
        colnames = [desc[0] for desc in self.__cur.description]
        for i in colnames:
            output += "|{}|".format(i.ljust(6))
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
            output += "|{}|".format(i.ljust(6))
        output +="\n"
        for team in self.__cur:
            output += '{}|{}|{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10), team[2].ljust(10), team[3].ljust(10))
        return output

q = Queries()

while q.input != 0:
    q.menu_selection()
    if q.input == "0":
        break
    elif q.input == "1":
        q.optionA()
        if q.input == "1":
            pass
        elif q.input == "2":
            pass
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
            pass
        elif q.input == "0":
            q.input = -1
        elif q.input > 3 or q.input < 0:
            print("Bad Input!")

    else:
        print("Bad Input!")
