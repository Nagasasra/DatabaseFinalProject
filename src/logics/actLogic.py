from src.utils.db import getDb

def getArrivals():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT arrival.*, book.bookTitle, CONCAT(employee.firstName, " ", employee.lastName) as employeeName
			FROM arrival
			JOIN book on arrival.bookId = book.bookid
			JOIN employee on arrival.employeeId = employee.employeeId
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addArrivals(arrival, employeeId):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `arrival`(`bookId`, `dateArrived`, `timeArrived`, `quantity`, `employeeId`) 
			VALUES (%s, %s, %s, %s, %s )
			;
		"""
	values = [arrival["bookId"], arrival["dateArrived"], arrival["timeArrived"], arrival["quantity"], employeeId]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Arrival record already registered"

	query = """
			SELECT bookQuantityTotal, bookQuantityAvailable FROM book WHERE bookid = %s
		"""
	values = [arrival["bookId"]]
	cursor.execute(query, tuple(values))
	book = cursor.fetchone()
	
	newQtyTotal = book["bookQuantityTotal"] + int(arrival["quantity"])
	newQtyAvailable = book["bookQuantityAvailable"] + int(arrival["quantity"])

	query = """
			UPDATE book SET bookQuantityTotal = %s, bookQuantityAvailable = %s WHERE bookid = %s
		"""
	values = [newQtyTotal, newQtyAvailable, arrival["bookId"]]
	cursor.execute(query, tuple(values))

	db.commit()

	return "success"

def getLendings():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT lending.*, 
				book.bookTitle, 
				CONCAT(employee.firstName, " ", employee.lastName) as employeeName, 
				CONCAT(customer.firstName, " ", customer.lastName) as customerName
			FROM lending
			JOIN book on lending.bookId = book.bookid
			JOIN employee on lending.employeeId = employee.employeeId
			JOIN customer on lending.customerId = customer.customerId
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def getLending(lendId):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT lending.*, 
				book.bookTitle, 
				CONCAT(employee.firstName, " ", employee.lastName) as employeeName, 
				CONCAT(customer.firstName, " ", customer.lastName) as customerName
			FROM lending
			JOIN book on lending.bookId = book.bookid
			JOIN employee on lending.employeeId = employee.employeeId
			JOIN customer on lending.customerId = customer.customerId
			WHERE lendId = %s
			;
		"""
	values = [lendId]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	#print(res)

	return res

def addLendings(lending, employeeId):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `lending`( `dateBorrowed`, `dueDate`, `bookId`, `employeeId`, `customerId`)
			VALUES (%s, %s, %s, %s, %s)			;
		"""
	values = [lending["dateBorrowed"], lending["dueDate"], lending["bookId"], employeeId, lending["customerId"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Lending record already registered"

	query = """
			SELECT bookQuantityAvailable FROM book WHERE bookid = %s
		"""
	values = [lending["bookId"]]
	cursor.execute(query, tuple(values))
	book = cursor.fetchone()
	
	newQtyAvailable = book["bookQuantityAvailable"] - 1
	if newQtyAvailable < 0:
		db.rollback()
		return "Book not available"

	query = """
			UPDATE book SET bookQuantityAvailable = %s WHERE bookid = %s
		"""
	values = [newQtyAvailable, lending["bookId"]]
	cursor.execute(query, tuple(values))

	db.commit()
	return "success"

def editLendings(lending):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """
			UPDATE lending SET dateReturned = %s, status = %s, charge = %s WHERE lendId = %s
		"""
	values = [lending["dateReturned"], lending["status"], lending["charge"], lending["lendId"]]
	cursor.execute(query, tuple(values))

	query = """
			SELECT bookQuantityAvailable FROM book WHERE bookid = %s
		"""
	values = [lending["bookId"]]
	cursor.execute(query, tuple(values))
	book = cursor.fetchone()
	
	newQtyAvailable = book["bookQuantityAvailable"] + 1

	query = """
			UPDATE book SET bookQuantityAvailable = %s WHERE bookid = %s
		"""
	values = [newQtyAvailable, lending["bookId"]]
	cursor.execute(query, tuple(values))

	db.commit()
	return "success"

def getSellings():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT selling.*,
				book.bookTitle,
				book.bookSellPrice,
				employee.employeeId,
				customer.customerId,
				CONCAT(employee.firstName, " ", employee.lastName) as employeeName, 
				CONCAT(customer.firstName, " ", customer.lastName) as customerName
			FROM selling
			JOIN book on selling.bookId = book.bookid
			JOIN employee on selling.employeeId = employee.employeeId
			JOIN customer on selling.customerId = customer.customerId
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addSellings(selling, price):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `selling`(`sellId`, `dateSold`, `timeSold`, `bookId`, `employeeId`, `customerId`, `price`)
			VALUES (%s, %s, %s, %s, %s, %s, %s);
		"""
	values = [selling["sellId"], selling["dateSold"], selling["timeSold"], selling["bookId"], selling["employeeId"], selling["customerId"], price]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Lending record already registered"
	db.commit()

	return "success"