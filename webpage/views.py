from webpage import app
from flask import render_template


@app.route("/") 
def reuven_page():
    return render_template('index.html')
