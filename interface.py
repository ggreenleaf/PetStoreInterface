# python interface to petstore mysql database
import mysql.connector

def update(cursor):
	pass

def delete(cursor):
	pass

def insert(cursor):
	pass

def select(cursor):
	tables = ["Pet_Store","Employs","Employee","Sells","Product","Stocks"]
	
	print "Please select a valid table to display information from"
	
	for i, table in enumerate(tables):
		print i,table

	while True:
		choice = int(raw_input("Enter number next to table: >>"))
		if choice < 0 or choice > len(tables) - 1:
			print "invalid entry"
			continue
		else:
			break

	query = "Select * from %s" % tables[choice]
	cursor.execute(query)

	for item in cursor:
		print item





	



def display_prompt():
	print """Welcome to the interface to petstore 
		Please type number of the operation you would like to perform
		1)	Insert a new value into the database
		2)	Delete a value from the database
		3)	Modify a current value in the database.
		4)	View table information
		5)	disconnect"""


cnx = mysql.connector.connect(user='root', database='PET_STORE_INVENTORY')
cur = cnx.cursor(buffer)

while True:
	display_prompt()
	choice = int(raw_input("Select your operation >> "))
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






	
			

	

		


