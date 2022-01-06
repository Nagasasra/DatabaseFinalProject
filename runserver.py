from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os
from src.routers.test import test_url
from src.routers.auth import auth_url
from src.routers.book import book_url
from src.routers.act import act_url
from src.routers.people import people_url


app = Flask(__name__, template_folder="src/views")

app.register_blueprint(test_url, url_prefix="/test")
app.register_blueprint(auth_url, url_prefix="")
app.register_blueprint(book_url, url_prefix="")
app.register_blueprint(act_url, url_prefix="")
app.register_blueprint(people_url, url_prefix="")

if __name__ == '__main__':
	app.secret_key = os.getenv("SECRETKEY")
	app.run(port=5000, debug=True)
	