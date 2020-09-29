# Class implementation pending 

# TESTED ON AWS RDS INSTANCE(WORKING)

import MySQLdb,sys
import getpass

# CONSTANTS
HOST="database-2.c3bnzrxiuxf0.ap-south-1.rds.amazonaws.com"
DATABASE="game"
USER="admin"
PASSWORD=getpass.getpass("Enter Password: ")
#


def dbconnect():
	try:
		conn = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DATABASE)
		return(conn)
	except Exception as e:
		print("Error connecting to db")
		sys.exit(1)
	
