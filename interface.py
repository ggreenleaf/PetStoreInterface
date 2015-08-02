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

def display_tables():
	for i, table in enumerate(tables):
		print i,table[0]

def update(cursor):
	pass

def delete(cursor):
	

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
	display_tables()
	choice = raw_input("Please enter the number for the table you would like to insert into: ")
	while True:
		try:
			if int(choice) < 0 or int(choice) > len(tables) - 1:
				print "please select a valid table number. You entered %d",int(choice)
				choice = raw_input("Please enter a valid number: ")
		except ValueError:
			print "please enter a number.You entered %s."%choice
			choice = raw_input("Please enter a number: ")


		else:
			break

	#gathering values for attributes.
	print "Inserting into table %s" %tables[int(choice)][0]
	print "please enter the data for the attribute listed"
	data_tuple = tuple([raw_input("%s: "%attribute) for attribute in tables[int(choice)][1]])
	att_length = len(tables[int(choice)][1])
	insert_sql = (
			"INSERT INTO %s (%s) "
			"Values (%s)" )%(tables[int(choice)][0] , 
							",".join(i for i in tables[int(choice)][1]),
							",".join(["%s" for i in xrange(att_length)]))
	
	cursor.execute(insert_sql,data_tuple)



def select(cursor):
	print "Please select a valid table to display information from"
	display_tables()
	while True:
		choice = int(raw_input("Enter number next to table: "))
		if choice < 0 or choice > len(tables) - 1:
			print "invalid entry"
			continue
		else:
			break

	query = "Select * from %s" % tables[choice][0]
	cursor.execute(query)
	print "\t".join(i for i in tables[choice][1])
	for t in cursor:
			print "\t".join(str(att) for att in t)


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
		pass

	elif choice == 2:
		pass

	elif choice == 3:
		pass

	elif choice == 4:
		select(cur)

	elif choice == 5:
		break

	cnx.commit() #commit changes after all operations incase view is selected after modifying DB

cnx.close()



	
			

	

		


