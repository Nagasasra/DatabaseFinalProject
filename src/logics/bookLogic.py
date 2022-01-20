from src.utils.db import getDb

def getBook(bookid):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT book.*, CONCAT(author.firstName, " ", author.lastName) as authorName, publisher.publisherName, genre.genreName
			FROM book 
			JOIN author on book.authorId = author.authorId
			JOIN publisher on book.publisherId = publisher.publisherId
			JOIN genre on book.genreId = genre.genreId
			WHERE bookid = %s
			;
		"""
	values = [bookid]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	#print(res)

	return res

def getBooks():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT book.*, CONCAT(author.firstName, " ", author.lastName) as authorName, publisher.publisherName, genre.genreName
			FROM book 
			JOIN author on book.authorId = author.authorId
			JOIN publisher on book.publisherId = publisher.publisherId
			JOIN genre on book.genreId = genre.genreId
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def addBooks(book):
	print(book)
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `book`(`bookid`, `bookPicture`, `bookTitle`, `bookReleaseYear`, `authorId`, `publisherId`, `genreId`, `bookLanguage`, `bookPages`, `bookQuantityTotal`, `bookQuantityAvailable`, `bookPrice`, `bookSellPrice`) 
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
			;
		"""
	values = [book["bookid"], book["bookPicture"], book["bookTitle"], book["bookReleaseYear"], book["authorId"], book["publisherId"], book["genreId"], book["bookLanguage"], book["bookPages"], 0, 0, book["bookPrice"], book["bookSellPrice"]]
	
	cursor.execute(query, tuple(values))
	try:
		pass
	except Exception as e:
		return "Book already registered"
	db.commit()

	return "success"

def editBooks(book, bookid):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """
			UPDATE book SET bookPrice = %s, bookSellPrice = %s WHERE bookid = %s
		"""
	values = [book["bookPrice"], book["bookSellPrice"], bookid]
	cursor.execute(query, tuple(values))
	book = cursor.fetchone()

	db.commit()
	return "success"

def editBooksPicture(bookPicture, bookid):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """
			UPDATE book SET bookPicture = %s WHERE bookid = %s
		"""
	values = [bookPicture, bookid]
	cursor.execute(query, tuple(values))
	book = cursor.fetchone()

	db.commit()
	return "success"

def getAuthor(authorId):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM author
			WHERE authorId = %s;
		"""
	values = [authorId]
	cursor.execute(query, tuple(values))
	res = cursor.fetchone()
	print(res)

	return res

def getAuthors():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT author.*, COUNT(book.bookid) as numBooks FROM author
			LEFT JOIN book on book.authorId = author.authorId
			GROUP BY firstName, lastName, dateofBirth, gender, emailAddress, nationality, preferredLanguage
			ORDER BY authorId
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	print(res)

	return res

def addAuthors(author):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `author`(`firstName`, `lastName`, `dateofBirth`, `gender`, `emailAddress`, `nationality`, `preferredLanguage`)
			VALUES (%s, %s, %s, %s, %s, %s, %s)
			;
		"""
	values = [author["firstName"], author["lastName"], author["dateofBirth"], author["gender"], author["emailAddress"], author["nationality"], author["preferredLanguage"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Author already registered"
	db.commit()

	return "success"

def getPublisher(publisherId):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM publisher
			WHERE publisherId;
		"""
	values = [publisherId]
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res

def getPublishers():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT publisher.*, COUNT(book.bookid) as numBooks FROM publisher
			LEFT JOIN book on book.publisherId = publisher.publisherId
			GROUP BY publisherName, publisherHeadquarter, publisherFullAddress, publisherEstablishedYear
			ORDER BY authorId
			;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

	return res


def addPublishers(publisher):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `publisher`(`publisherName`, `publisherHeadquarter`, `publisherFullAddress`, `publisherEstablishedYear`)
			VALUES (%s, %s, %s, %s)
			;
		"""
	values = [publisher["publisherName"], publisher["publisherHeadquarter"], publisher["publisherFullAddress"], publisher["publisherEstablishedYear"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Publisher already registered"
	db.commit()

	return "success"


def getGenres():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT COUNT(book.bookid) as numBooks, genre.genreId, genre.genreName, genre.genreDescription FROM genre
			LEFT JOIN book on book.genreId = genre.genreId
			GROUP BY genreName, genreDescription
			ORDER BY genreName
			;
		"""

	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()

	print(res)
	return res

def addGenres(genre):
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `genre`(`genreName`, `genreDescription`) VALUES (%s, %s)
			;
		"""
	values = [genre["genreName"], genre["genreDescription"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Genre already registered"
	db.commit()

	return "success"