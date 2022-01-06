from flask import Blueprint, render_template, jsonify, request, session
import src.logics.testLogic as testLogic

test_url = Blueprint("user", __name__)

@test_url.route("/register", methods=["GET"])
def register_user():
	return "Hello test"

@test_url.route("/hello", methods=["GET"])
@test_url.route("/hello/<name>", methods=["GET"])
def login_user(name = None):
	if name:
		session['username'] = "Username" + name
	#else:
	#	session['username'] = "Username"
	return render_template("hello.html", name2=name)

@test_url.route("/db", methods=["GET"])
def db():
	data = testLogic.db()
	#return jsonify(data)
	return jsonify(data)