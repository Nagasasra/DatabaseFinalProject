from src.utils.db import getDb

def getCustomers():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM customer;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addCustomers(customer):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `customer`(`FirstName`, `LastName`, `dateofBirth`, `gender`, `phoneNumber`, `emailAddress`)
			VALUES (%s, %s, %s, %s, %s, %s)
			;
		"""
	values = [customer["FirstName"], customer["LastName"], customer["dateofBirth"], customer["gender"], customer["phoneNumber"], customer["emailAddress"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Customer already registered"
	db.commit()

	return "success"

def getEmployees():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM employee LEFT JOIN user
			on user.employeeId = employee.employeeId;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addEmployees(employee):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `employee`(`FirstName`, `LastName`, `dateofBirth`, `gender`, `phoneNumber`, `emailAddress`, `homeAddress`)
			VALUES (%s, %s, %s, %s, %s, %s, %s)
			;
		"""
	values = [employee["FirstName"], employee["LastName"], employee["dateofBirth"], employee["gender"], employee["phoneNumber"], employee["emailAddress"], employee["homeAddress"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Employee already registered"
	db.commit()

	return "success"