from flask import Flask
from v_connect import dbconnect
app = Flask(__name__)

# ALLOWED VALUES FOR STATUS "In-Progress","Not-Initiated","Pending","Completed"
@app.route('/items/<status>')
def get_item(status):
	conn = dbconnect()
	cur = conn.cursor()
	types = ["In-Progress","Not-Initiated","Pending","Completed"]
	if status not in types:
		return("Invalid Parameter")

	cur.execute("select * from Task where Status='{}' LIMIT 1;".format(status))
	# get returned column names from the cursor. 
	columns = [i[0] for i in cur.description]
	# print('\ncolumns:\n'+'#'*10, "\n".join(columns), '#'*10+'\n', sep='\n')

	result = {}
	for index, col_name in enumerate(cur.fetchone()):
		result[columns[index]] = col_name

	conn.close()
	return result


@app.route('/items')
def get_items():
	conn = dbconnect()
	cur = conn.cursor()
	cur.execute("select * from Task;")
	columns = [i[0] for i in cur.description]
	results = []
	for row in cur.fetchall():
		result = {}
		for index, col_name in enumerate(row)
			result[columns[index]] = col_name
		results.append(result)
		

	conn.close()
	return {"data":results}


if __name__ == '__main__':
    app.run()
