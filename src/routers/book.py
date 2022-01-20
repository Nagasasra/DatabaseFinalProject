from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.bookLogic as bookLogic

book_url = Blueprint("book", __name__)

@book_url.route("/books", methods=["GET"])
def view_books():
	if session.get('username', None) == None:
		return redirect("/login")
	books = bookLogic.getBooks()
	return render_template("books.html", books = books)

@book_url.route("/books/add", methods=["GET"])
def add_books(msg=""):
	if session.get('username', None) == None:
		return redirect("/login")

	authors = bookLogic.getAuthors()
	publishers = bookLogic.getPublishers()
	genres = bookLogic.getGenres()
	return render_template("addBook.html", authors = authors, publishers = publishers, genres = genres, errorMessage=msg)

@book_url.route("/books/add", methods=["POST"])
def add_books_post():
	if session.get('username', None) == None:
		return redirect("/login")

	file = request.files['bookPicture']
	new_form = dict(request.form)
	new_form['bookPicture'] = None
	if file.filename != '':
		filename = request.form.get("bookid") + "." + file.filename.split(".")[-1].lower()
		file.save("static/books/" + filename)
		new_form['bookPicture'] = filename

	if request.form.get("bookid"):
		is_success = bookLogic.addBooks(new_form)
		print(is_success)
		if is_success == "success":
			return redirect("/books")

	return add_books(is_success)

@book_url.route("/books/edit/<bookid>", methods=["GET"])
def edit_books(bookid):
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""

	book = bookLogic.getBook(bookid)
	return render_template("editBook.html", book = book, errorMessage=is_success)

@book_url.route("/books/edit/<bookid>", methods=["POST"])
def edit_books_post(bookid):
	print(request.form)
	if session.get('username', None) == None:
		return redirect("/login")
	file = request.files['bookPicture']
	if file.filename != '':
		filename = request.form.get("bookid") + "." + file.filename.split(".")[-1].lower()
		file.save("static/books/" + filename)
		bookLogic.editBooksPicture(filename, request.form.get("bookid"))
		
	is_success = ""
	if request.form.get("bookid"):
		is_success = bookLogic.editBooks(request.form, bookid)
		if is_success == "success":
			return redirect("/books")

	book = bookLogic.getBook(bookid)
	return render_template("editBook.html", book = book, errorMessage=is_success)

@book_url.route("/authors", methods=["GET"])
def view_authors():
	if session.get('username', None) == None:
		return redirect("/login")
	authors = bookLogic.getAuthors()
	return render_template("authors.html", authors = authors)

@book_url.route("/authors/add", methods=["GET"])
def add_authors():
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if request.args.get("emailAddress"):
		is_success = bookLogic.addAuthors(request.args)
		if is_success == "success":
			return redirect("/authors")

	return render_template("addAuthor.html", errorMessage=is_success)

@book_url.route("/authors/edit/<authorId>", methods=["GET"])
def edit_authors(authorId):
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if request.args.get("authorId"):
		is_success = bookLogic.edit_authors(request.args)
		if is_success == "success":
			return redirect("/authorId")

	author = bookLogic.getAuthor(authorId)
	return render_template("edit_authors.html", author = author, errorMessage=is_success)

@book_url.route("/publishers", methods=["GET"])
def view_publishers():
	if session.get('username', None) == None:
		return redirect("/login")
	publishers = bookLogic.getPublishers()
	return render_template("publishers.html", publishers = publishers)

@book_url.route("/publishers/add", methods=["GET"])
def add_publishers():
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if request.args.get("publisherName"):
		is_success = bookLogic.addPublishers(request.args)
		if is_success == "success":
			return redirect("/publishers")

	publishers = bookLogic.getPublishers()
	return render_template("addPublisher.html", publishers = publishers, errorMessage=is_success)

@book_url.route("/publishers/edit/<publisherId>", methods=["GET"])
def edit_publishers(publisherId):
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if request.args.get("publisherId"):
		is_success = bookLogic.edit_publishers(request.args)
		if is_success == "success":
			return redirect("/publisherId")

	publisher = bookLogic.getPublisher(publisherId)
	return render_template("edit_publishers.html", publisher = publisher, errorMessage=is_success)

@book_url.route("/genres", methods=["GET"])
def view_genres():
	if session.get('username', None) == None:
		return redirect("/login")
	genres = bookLogic.getGenres()
	return render_template("genres.html", genres = genres)

@book_url.route("/genres/add", methods=["GET"])
def add_genres():
	if session.get('username', None) == None:
		return redirect("/login")
	if request.args.get("genreName"):
		is_success = bookLogic.addGenres(request.args)
		if is_success == "success":
			return redirect("/genres")

	genres = bookLogic.getGenres()
	return render_template("addGenre.html", genres = genres)