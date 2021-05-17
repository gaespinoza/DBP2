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
            "1 - Teams on Specified League \n" \
            "2 - Teams Owned by User \n" \
            "3 - Overall Score for Team \n" \
            "4 - Add New League With Manager \n" \
            "5 - Create a New User\n" \
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
        output += "colnames\n"
        for team in self.__cur:
            output += '{}|{}|{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10), team[2].ljust(10), team[3].ljust(10))
        return output

q = Queries()

while q.input != 0:
	q.menu_selection()
	if q.input == "0":
		break
	elif q.input == "1":
	    print(q.league_team())
	elif q.input == "2":
	    print(q.hire())
	elif q.input == "3":
	    print(q.transcript())
	elif q.input == "4":
	    print(q.course_list())
	elif q.input == "5":
	    print(q.register())
	else:
	    print("Bad Input!")
