from src.utils.db import getDb

def db():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = "SELECT * FROM user;"
	cursor.execute(query, ())
	res = cursor.fetchall()
	return res