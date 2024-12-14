from flask import Flask

app = Flask(__name__)



from webpage.views import reuven_page

# @app.route("/")
# def home_page():
#     return "Welcome to the Home Page!"

