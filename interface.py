# python interface to petstore mysql database
import mysql.connector

tables = [("PET_STORE",("sid","StreetNo","StreetName","City","State","PhoneNumber")),
				("JOB", ("JobDesc","PayRate")),
				("WORKS",("Eid","JobDesc","Hours")),
				("P_TRANSACTION",("Tid","Date")),
				("EXECUTES",("Eid","Tid","TerminalNo")),
				("Employee",("Eid","FirstName","LastName")),
				("Employs",("Eid","Sid","StartDate")),
				("PRODUCT",("Pid","Name","Description","Price")),
				("STOCKS",("Sid","Pid","Quantity")),
				("SELLS",("Tid","Pid","Quantity"))]


def update(cursor):
	pass

def delete(cursor):
	pass

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
	pass

def select(cursor):

	
	print "Please select a valid table to display information from"
	
	for i, table in enumerate(tables):
		print i,table[0]

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
			print "\t".join(str(att) for att in t)git 


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
		pass

	elif choice == 2:
		pass

	elif choice == 3:
		pass

	elif choice == 4:
		select(cur)

	elif choice == 5:
		break






	
			

	

		


