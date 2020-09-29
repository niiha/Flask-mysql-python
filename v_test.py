from flask import Flask, redirect, url_for, request
from uuid import uuid4
from flask_mysqldb import MySQL
from getpass import getpass

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-2.c3bnzrxiuxf0.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'atmecs123' # getpass("Enter Password: ")
app.config['MYSQL_DB'] = 'game'

mysql = MySQL(app)


# GLOBALS:
UUID = None


@app.route('/')
def hw():
	return "READY " + str(UUID), 201

@app.route('/play')
def hw1():
	token = request.args.get('token')
	col = int(request.args.get('col'))
	if not token or not col:
		return "Pass 'col' and 'token' as query parameters"
	if not(col>=0 and col<=6):
		return "INVALID"
	return "READY " + str(col)+token, 201

@app.route('/START')
def hw2():
	global UUID 
	UUID = str(uuid4())
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO conn4 (ID) VALUES ('{}');".format(UUID))
	mysql.connection.commit()
	cur.close()
	return redirect(url_for('hw'))





# # ALLOWED VALUES FOR STATUS "In-Progress","Not-Initiated","Pending","Completed"
# @app.route('/items/<status>')
# def get_item(status):
# 	conn = dbconnect()
# 	cur = conn.cursor()
# 	types = ["In-Progress","Not-Initiated","Pending","Completed"]
# 	if status not in types:
# 		return("Invalid Parameter")

# 	cur.execute("select * from Task where Status='{}' LIMIT 1;".format(status))
# 	# get returned column names from the cursor. 
# 	columns = [i[0] for i in cur.description]
# 	# print('\ncolumns:\n'+'#'*10, "\n".join(columns), '#'*10+'\n', sep='\n')

# 	result = {}
# 	for index, col_name in enumerate(cur.fetchone()):
# 		result[columns[index]] = col_name

# 	conn.close()
# 	return result


# @app.route('/items')
# def get_items():
# 	conn = dbconnect()
# 	cur = conn.cursor()
# 	cur.execute("select * from Task;")
# 	columns = [i[0] for i in cur.description]
# 	results = []
# 	for row in cur.fetchall():
# 		result = {}
# 		for index, col_name in enumerate(row):
# 			result[columns[index]] = col_name
# 		results.append(result)
		

# 	conn.close()
# 	return {"data":results}


# if __name__ == '__main__':
#     app.run()
