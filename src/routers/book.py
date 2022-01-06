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
def add_books():
	if session.get('username', None) == None:
		return redirect("/login")
	if request.args.get("bookid"):
		is_success = bookLogic.addBooks(request.args)
		print(is_success)
		if is_success == "success":
			return redirect("/books")

	authors = bookLogic.getAuthors()
	publishers = bookLogic.getPublishers()
	genres = bookLogic.getGenres()
	return render_template("addBook.html", authors = authors, publishers = publishers, genres = genres)

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
	if request.args.get("emailAddress"):
		is_success = bookLogic.addAuthors(request.args)
		if is_success == "success":
			return redirect("/authors")

	return render_template("addAuthor.html")

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
	if request.args.get("publisherName"):
		is_success = bookLogic.addPublishers(request.args)
		if is_success == "success":
			return redirect("/publishers")

	publishers = bookLogic.getPublishers()
	return render_template("addPublisher.html", publishers = publishers)

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