# Class implementation pending 

# TESTED ON AWS RDS INSTANCE(WORKING)

import MySQLdb,sys
import getpass

# CONSTANTS
HOST="DB_ENDPOINT/HOSTNAME_GOES_HERE"
DATABASE="DB_NAME_GOES_HERE"
USER="DB_USERNAME_GOES_HERE"
PASSWORD=getpass.getpass("Enter Password: ")
#


def dbconnect():
	try:
		conn = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DATABASE)
		return(conn)
	except Exception as e:
		print("Error connecting to db")
		sys.exit(1)
	
