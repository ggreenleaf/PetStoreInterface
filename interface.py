# python interface to petstore mysql database
import mysql.connector

tables = (("PET_STORE",("sid","StreetNo","StreetName","City","State","phone_number")),
				("JOB", ("JobDesc","PayRate")),
				("WORKS",("eid","JobDesc","Hours")),
				("P_TRANSACTION",("tid","tDate")),
				("EXECUTES",("eid","tid","terminalNo")),
				("Employee",("eid","fName","lname")),
				("Employs",("eid","sid","startDate")),
				("PRODUCT",("pid","pname","pdesc","price")),
				("STOCKS",("sid","pid","quantity")),
				("SELLS",("tid","pid","t_quantity")))


def get_choice(upper_bound):
	'''will return a valid integer choice between [0,upper_bound)'''
	choice = raw_input("Please enter a valid number: ")
	while True:
		try:
			if int(choice) < 0 or int(choice) > upper_bound:
				print "please select a valid table number. You entered ",int(choice)
				choice = raw_input("Please enter a valid number: ")
			else:
				break
		except ValueError:
			print "please enter a number.You entered %s."%choice
			choice = raw_input("Please enter a number: ")

	return int(choice)

def display_tables():
	for i, table in enumerate(tables):
		print i,table[0]


def get_table_choice():
	display_tables()

	choice = get_choice(len(tables))
	return choice

def modify(cursor):
	#Modify alg
	#display tables/select
	#select valid entry to update
	#input new value
	#create sql
	#execute sql

	choice = get_table_choice()
	query = "Select * from %s" % tables[choice][0]
	cursor.execute(query)
	print "  ","\t".join(i for i in tables[choice][1])
	saved_data = []
	for i,t in enumerate(cursor):
			print "%d)"%i, "\t".join(str(att) for att in t)
			saved_data.append(t)

	tuple_choice = get_choice(len(saved_data))
	print "updating entry:\n\t%s\n Please enter the new values you wish to change"%(" ".join(str(val) for val in saved_data[tuple_choice]))
	print "To keep the same value reenter the same value"
	update_cond = tuple(raw_input("%s: "%attribute) for attribute in tables[choice][1])
	update_sql = (
			"UPDATE %s SET %s WHERE (%s)")%(tables[choice][0],
				", ".join("%s='%s'"%(col,val) for col,val in zip(tables[choice][1],update_cond)),
				" AND ".join("%s='%s'"%(col,val) for col,val in zip(tables[choice][1],saved_data[tuple_choice])))
	cursor.execute(update_sql)
	

def delete(cursor):
	choice = get_table_choice()
	query = "Select * from %s" % tables[choice][0]
	cursor.execute(query)
	print "  ","\t".join(i for i in tables[choice][1])
	saved_data = []
	for i,t in enumerate(cursor):
			print "%d)"%i, "\t".join(str(att) for att in t)
			saved_data.append(t)

	tuple_choice = get_choice(i) 
	delete_cond = tuple("%s='%s'"%(col,val) for col,val in zip(tables[choice][1],saved_data[tuple_choice]))
	delete_sql = (
		"DELETE FROM %s "
		"WHERE (%s)")%(tables[choice][0],"AND ".join(i for i in delete_cond))
	cursor.execute(delete_sql)


def insert(cursor):
	#Example of a insert command
	##testing insert
	#
	#insert = (
	#	"INSERT INTO PET_STORE (sid,StreeNo,StreetName,City,State,Phone_number) "
	#	"VALUES (%s, %s, %s, %s, %s, %s, %s)" )
	# cursor.execute(insert,(tuple of values for insert))
	# 
	#cnx.commit() will save the changes
	#
	#
	choice = get_table_choice()

	#gathering values for attributes.
	print "Inserting into table %s" %tables[choice][0]
	print "please enter the data for the attribute listed"
	data_tuple = tuple(raw_input("%s: "%attribute) for attribute in tables[choice][1])
	att_length = len(tables[choice][1])
	insert_sql = (
			"INSERT INTO %s (%s) "
			"Values (%s)" )%(tables[choice][0] , 
							",".join(i for i in tables[choice][1]),
							",".join(["%s" for i in xrange(att_length)]))
	
	cursor.execute(insert_sql,data_tuple)


def select(cursor):
	print "Please select a valid table to display information from"
	# display_tables()
	# while True:
	# 	choice = int(raw_input("Enter number next to table: "))
	# 	if choice < 0 or choice > len(tables) - 1:
	# 		print "invalid entry"
	# 		continue
	# 	else:
	# 		break
	choice = get_table_choice()
	query = "Select * from %s" % tables[choice][0]
	cursor.execute(query)
	print "  ","\t".join(i for i in tables[choice][1])
	for i,t in enumerate(cursor):
			print "%d)"%i, "\t".join(str(att) for att in t)
	

def display_prompt():
	print """Welcome to the interface to petstore 
		Please type number of the operation you would like to perform
		1)	Insert a new value into the database
		2)	Delete a value from the database
		3)	Modify a current value in the database.
		4)	View table information
		5)	disconnect"""


cnx = mysql.connector.connect(user='root', database='PET_STORE_2')
cur = cnx.cursor(buffered=True)

while True:
	display_prompt()
	choice = int(raw_input("Select your operation: "))
	if choice < 1 or choice > 5:
		print "You have selected an invalid operation please choose a valid operation."
		continue 

	if choice == 1:
		insert(cur)

	elif choice == 2:
		delete(cur)

	elif choice == 3:
		modify(cur)

	elif choice == 4:
		select(cur)

	elif choice == 5:
		break

	cnx.commit() #commit changes after all operations incase view is selected after modifying DB

cnx.close()



	
			

	

		


