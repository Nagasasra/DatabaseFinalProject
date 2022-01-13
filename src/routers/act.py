from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.actLogic as actLogic
import src.logics.bookLogic as bookLogic
import src.logics.peopleLogic as peopleLogic

act_url = Blueprint("activity", __name__)

@act_url.route("/arrivals", methods=["GET"])
def view_arrivals():
	if session.get('username', None) == None:
		return redirect("/login")
	arrivals = actLogic.getArrivals()
	return render_template("arrivals.html", arrivals = arrivals)

@act_url.route("/arrivals/add", methods=["GET"])
def add_arrivals():
	if session.get('username', None) == None:
		return redirect("/login")
	if request.args.get("bookId"):
		print(request.args)
		is_success = actLogic.addArrivals(request.args, session["employeeId"])
		if is_success == "success":
			return redirect("/arrivals")

	books = bookLogic.getBooks()

	return render_template("addArrival.html", books = books)

@act_url.route("/lendings", methods=["GET"])
def view_lendings():
	if session.get('username', None) == None:
		return redirect("/login")
	lendings = actLogic.getLendings()
	return render_template("lendings.html", lendings = lendings)

@act_url.route("/lendings/add", methods=["GET"])
def add_lendings():
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if request.args.get("bookId"):
		is_success = actLogic.addLendings(request.args, session["employeeId"])
		if is_success == "success":
			return redirect("/lendings")

	books = bookLogic.getBooks()
	customers = peopleLogic.getCustomers()
	return render_template("addLending.html", books = books, customers = customers, errorMessage=is_success)

@act_url.route("/lendings/edit/<lendId>", methods=["GET"])
def edit_lendings(lendId):
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if request.args.get("lendId"):
		is_success = actLogic.editLendings(request.args)
		if is_success == "success":
			return redirect("/lendings")

	lending = actLogic.getLending(lendId)
	return render_template("editLending.html", lending = lending, errorMessage=is_success)

@act_url.route("/sellings", methods=["GET"])
def view_sellings():
	if session.get('username', None) == None:
		return redirect("/login")
	sellings = actLogic.getSellings()
	return render_template("sellings.html", sellings = sellings)

@act_url.route("/sellings/add", methods=["GET"])
def add_sellings():
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if request.args.get("bookId"):
		is_success = actLogic.addSellings(request.args, session["employeeId"])
		if is_success == "success":
			return redirect("/sellings")

	books = bookLogic.getBooks()
	customers = peopleLogic.getCustomers()
	sellings = actLogic.getSellings()
	return render_template("addSelling.html", books = books, customers = customers, sellings = sellings, errorMessage=is_success)

@act_url.route("/financial", methods=["GET"])
def view_finance():
	if session.get('username', None) == None:
		return redirect("/login")
	finances = actLogic.getFinance()
	return render_template("financial.html", finances = finances)