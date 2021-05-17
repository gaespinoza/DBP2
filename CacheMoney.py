import psycopg2

# sems = {'spring':'Spring', 'summer':'Summer','fall':'Fall','winter':'Winter'}


class Queries:
	def __init__(self):
		# self.__grades =  {'A':4, 'A-':3.7, 'B+':3.3, 'B':3, 'B-':2.7, \
		# 	'C+':2.3, 'C':2, 'C-':1.7, 'D+':1.3, 'D':1, 'D-':0.7, 'F':0}

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
		query = "select L.id as L_id, L.name as LeagueName, T.id as T_id, T.name as TeamName from league as L join team as T on L.id=T.league_id and L.id=%s;"
		self.__cur.execute(query)
		output += "Teams in League!\n"
		colnames = [desc[0] for desc in self.__cur.description]
		output += "colnames\n"
		for team in self.__cur:
			output += '{}|{}|{}|{}\n'.format(team[0].ljust(6), team[1].ljust(10), team[2].ljust(10), team[3].ljust(10))
		return output

	def hire(self):
		output = ""
		"""
	    primary - id in instructor must be unique
	    foreign - dept_name must exist department

	    if id is unique and dept_name in departments:
	        insert id, name, dept_name salary into instructor
	    """    
		new_id = input("ID of New Instructor: ") #int

		new_name = input("Name of New Instructor: ")

		new_dept_name = input("Department of New Instructor: ")
		q2 = "select * from department where dept_name = %s;"

		new_salary = input("Salary of New Instructor: ") #int

		insert_query = "insert into instructor values (%s, %s, %s, %s);"
		try:
		    self.__cur.execute(insert_query, (new_id, new_name, new_dept_name, new_salary,))
		    self.__conn.commit()
		except psycopg2.errors.UniqueViolation:
			output = "ERROR - ID value not numeric"
		except psycopg2.errors.ForeignKeyViolation:
			output = "ERROR - Department does not exist"
		except psycopg2.errors.CheckViolation:
			output = "ERROR - Salary value is too low"
		except psycopg2.errors.SyntaxError:
			output = "ERROR - letters placed in salary field"
		except Exception as e:
			output = str(e)
		return output

	def transcript(self):
		output = ""
		s_id = input("Enter Student ID: ")

		q1 = "select * from student where id = %s;"
		self.__cur.execute(q1, (s_id,))
		if self.__cur.rowcount == 0:
		    output = "ERROR - Student does not exist"
		    return output
		#transcript query
		tq = "select * from " \
		    "(select T.semester, T.year, T.grade, T.id, T.course_id, T.sec_id, " \
		    "S.name, S.dept_name, C.credits, C.title from student as S " \
		    "join takes as T on S.id=T.id join course as C on T.course_id=C.course_id)" \
		    " as Q where Q.id=%s order by Q.year, Q.semester desc;"

		try:
		    self.__cur.execute(tq, (s_id,))
		except Exception as e:
		    output = str(e)
		    return output
		#------------------------- output the table that has been returned properly -------------------------------

		credits_tot = 0
		quality = 0

		cur_sem = None
		i = 0
		sem_gpa = 0
		total = 0 
		sem = ''
		classes = []

		for row in self.__cur:
			if i == 0:
				output += f"\nStudent ID: {row[3]}\n"
				output += f"{row[6]}, {row[7]}\n"
			if row[0] != cur_sem:
				if i != 0:
					output += f"\n{sem} {round(sem_gpa/total,2)}\n\n"
					for c in classes:
						output += f"   {c}\n"
				output += f"{row[0]} {row[1]}\n"
				sem = f"{row[0]} {row[1]}"
				cur_sem = row[0]
				sem_gpa = 0
				total = 0
				classes = []
			classes.append(f"{row[4]}-{row[5]} {row[9]} ({row[8]}) {row[2]}")
			i+=1
			sem_gpa += (self.__grades[row[2]] * float(row[8]))
			total += (float(row[8]))
			quality += (self.__grades[row[2]] * float(row[8]))
			credits_tot += (float(row[8]))
		output += f"\n{sem} {round(sem_gpa/total,2)}\n\n"
		for c in classes:
			output += f"    {c}\n"
		output += f"\nCumulative GPA {round(quality/credits_tot,2)}\n\n"
		return output

	def course_list(self):
		output = ""
		semester = input("What semester will you like to look at? \ninput: ")

		year = input("What year will you like to look at? \ninput: ")


		query = "select * from (select C.course_id, C.title, C.credits, S.sec_id, S.semester, S.year, S.building, S.room_number, CL.capacity, TA.enrollment, S.time_slot_id "\
		    "from course as C " \
		    "join section as S on C.course_id = S.course_id "\
		    "join classroom as CL on S.building = CL.building and S.room_number = CL.room_number "\
		    "join ( select T.course_id, T.sec_id, T.semester, T.year, count(*) as enrollment from takes as T "\
		    "group by T.course_id, T.sec_id, T.semester, T.year) as TA on S.course_id = TA.course_id and S.sec_id = TA.sec_id and S.semester = TA.semester and S.year = TA.year) as Table1 "\
		    "where Table1.semester=%s and Table1.year=%s;"
		try:
			self.__cur.execute(query, (semester, year,))

			for row in self.__cur:
				formating = f"\n{row[0]}-{row[3]} {row[1]} ({row[2]}) {row[6]} {row[7]} {row[8]} {row[9]}"
				#sub query to get the time slot information more easily for formatting
				temp_conn = self.__conn.cursor()

				sub_q = "select * from time_slot where time_slot_id=%s;"

				temp_conn.execute(sub_q,(row[10],))
				for day in temp_conn:
					formating += f"\n {day[1]} {day[2]}:{int(day[3]):02d}-{day[4]}:{day[5]}"
				output += formating
		except psycopg2.errors.InvalidTextRepresentation:
			output = "ERROR: Please input a number for year"
		return output

	def register(self):
		output = ""

		output += "Register A Student!"
		print("Register A Student!")
		return output


	def __exec(query, inp, commit=0):
		try:
			self.__cur(query, inp)
		except Exception as e:
			print(e)
q = Queries()

while q.input != 0:
	q.menu_selection()
	if q.input == "0":
		break
	elif q.input == "1":
	    print(q.advisor_list())
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
