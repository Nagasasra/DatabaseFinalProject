from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.peopleLogic as peopleLogic

people_url = Blueprint("people", __name__)

@people_url.route("/customers", methods=["GET"])
def view_customers():
	if session.get('username', None) == None:
		return redirect("/login")
	customers = peopleLogic.getCustomers()
	return render_template("customers.html", customers = customers)

@people_url.route("/customers/add", methods=["GET"])
def add_customers():
	if session.get('username', None) == None:
		return redirect("/login")
	if request.args.get("emailAddress"):
		is_success = peopleLogic.addCustomers(request.args)
		if is_success == "success":
			return redirect("/customers")

	customers = peopleLogic.getCustomers()

	return render_template("addCustomer.html", customers = customers)

@people_url.route("/employees", methods=["GET"])
def view_employees():
	if session.get('username', None) == None:
		return redirect("/login")

	employees = peopleLogic.getEmployees()
	return render_template("employees.html", employees = employees)

@people_url.route("/employees/add", methods=["GET"])
def add_lendings():
	if session.get('username', None) == None:
		return redirect("/login")
	if request.args.get("emailAddress"):
		is_success = peopleLogic.addEmployees(request.args)
		if is_success == "success":
			return redirect("/employees")

	employees = peopleLogic.getEmployees()
	return render_template("addEmployee.html", employees = employees)
