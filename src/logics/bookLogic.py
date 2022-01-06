from src.utils.db import getDb

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
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			INSERT INTO `book`(`bookid`, `bookTitle`, `bookReleaseYear`, `authorId`, `publisherId`, `genreId`, `bookLanguage`, `bookPages`, `bookQuantityTotal`, `bookQuantityAvailable`, `bookPrice`, `bookSellPrice`) 
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
			;
		"""
	values = [book["bookid"], book["bookTitle"], book["bookReleaseYear"], book["authorId"], book["publisherId"], book["genreId"], book["bookLanguage"], book["bookPages"], 0, 0, book["bookPrice"], book["bookSellPrice"]]
	
	try:
		cursor.execute(query, tuple(values))
	except Exception as e:
		return "Book already registered"
	db.commit()

	return "success"



def getAuthors():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM author;
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



def getPublishers():
	db = getDb()
	cursor = db.cursor(dictionary=True)

	query = """ 
			SELECT * FROM publisher;
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
			SELECT * FROM genre;
		"""
	values = []
	cursor.execute(query, tuple(values))
	res = cursor.fetchall()
	#print(res)

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