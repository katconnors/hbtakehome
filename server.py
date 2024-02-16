from flask import Flask, render_template, request, redirect
from model import database_connect
import os
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route("/")
def homepage():
    """Site landing page"""

    return render_template("home.html")



@app.route("/view")
def viewres():
    """Viewing booked reservations"""

    return render_template("view.html")



@app.route("/book")
def bookres():
    """Booking a new reservation"""

    return render_template("book.html")



@app.route("/book")
def bookres():
    """Confirming that a new reservation was booked"""

    return render_template("confirmation.html")







if __name__ == "__main__":

    database_connect(app,"melonres")

    #important to disable debug later

    
    app.run(debug=True,host="0.0.0.0")
