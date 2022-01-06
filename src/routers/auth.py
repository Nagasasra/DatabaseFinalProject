from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.authLogic as authLogic

auth_url = Blueprint("auth", __name__)

@auth_url.route("/register", methods=["GET"])
def register_user():
	print(request.args)
	if request.args.get("email"):
		is_success = authLogic.register(request.args)
		if is_success == "success":
			return redirect("/login")
		else:
			return render_template("register.html", errorMessage=is_success)

	return render_template("register.html")

@auth_url.route("/login", methods=["GET"])
def login_user():
	print(request.args)
	if request.args.get("username"):
		is_success = authLogic.login(request.args)
		if is_success == "success":
			return redirect("/home")
		else:
			return render_template("login.html", errorMessage=is_success)

	return render_template("login.html")

@auth_url.route("/logout", methods=["GET"])
def logout_user():
	session.clear()
	return redirect("/login")

@auth_url.route("/home", methods=["GET"])
def home():
	if session.get('username', None) == None:
		return redirect("/login")
	return render_template("home.html")

@auth_url.route("/profile", methods=["GET"])
def profile():
	if session.get('username', None) == None:
		return redirect("/login")

	user = authLogic.getUser(session["username"])
	return render_template("profile.html", user = user)