from os import name
from flask import Flask, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World"

@app.route('/login/<string:email>/<string:password>')

def login(email,password):
	conn=sqlite3.connect("1.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM test WHERE email=? AND password=?",(email,password))
	row=cur.fetchall()
	conn.close()
	print(row)
	if row!=[]:
		user_name=row[0][1]
		return "user name found with name: "+user_name
	else:
		return "user not found "

@app.route('/signup_database/<string:name>/<string:email>/<string:password>')

def signup_database(name,email,password):
	conn=sqlite3.connect("1.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
	cur.execute("INSERT INTO test Values(Null,?,?,?)",(name,email,password))
	conn.commit()
	conn.close()



if __name__ == "__main__":
    app.run(debug=True)