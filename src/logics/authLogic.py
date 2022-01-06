from flask import session
from src.utils.db import getDb
import bcrypt

def register(userData):
	if userData["password"] != userData["password2"]:
		return "Password don't match"

	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = "SELECT * FROM employee WHERE emailAddress = %s;"
	values = [userData["email"]]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	print(res)

	if not res:
		return "Email not found"

	employeeId = res["employeeId"]
	pw_encrypted = bcrypt.hashpw(userData["password"].encode(), bcrypt.gensalt())

	query = "INSERT INTO user (username, password, employeeId) VALUES (%s, %s, %s);"
	values = [userData["username"], pw_encrypted, employeeId]

	try:
		affected_rows = cursor.execute(query, tuple(values))
	except Exception as e:
		return "User already registered"
	db.commit()

	return "success"

def login(userData):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = "SELECT * FROM user WHERE username = %s;"
	values = [userData["username"]]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	print(res)

	if not res:
		return "username not found"

	if not bcrypt.checkpw(userData["password"].encode(), res["password"].encode()):
		return "wrong password"

	session['username'] = res["username"]
	session['employeeId'] = res["employeeId"]
	return "success"

def getUser(username):
	db = getDb()
	cursor = db.cursor(dictionary=True)
	query = "SELECT * FROM user JOIN employee on employee.employeeId = user.employeeId WHERE username = %s;"
	values = [username]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	print(res)
	return res