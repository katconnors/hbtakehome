from flask import Flask, render_template, request, redirect, session
from model import database_connect
import os
from jinja2 import StrictUndefined
import crud


app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route("/")
def homepage():
    """Site landing page"""

    return render_template("home.html")



@app.route("/login")
def login():
    """Login page"""

    if request.args.get('username_input') or session.get('username'):

        if session.get('username'):
            if crud.user_in_db(session['username']):
                return redirect("/loginconfirmed")
        
        else:
            session['username'] = request.args.get('username_input')

            if crud.user_in_db(session['username']):
                return redirect("/loginconfirmed")
            else:
                return redirect('/log.html')
    else:
        return render_template("log.html")


@app.route("/loginconfirmed")
def login_confirm():
    """Post login confirmation"""

    return render_template("loggedin.html")


@app.route("/view")
def viewres():
    """User can view their previously booked reservations"""

    return render_template("view.html")



@app.route("/book")
def bookres():
    """Booking a new reservation
    Shows filtered results according to user entries"""

    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')
    date = request.args.get('date')

    return render_template("book.html",starttime=starttime,endtime=endtime,date=date)





@app.route("/confirmed")
def bookedconfirm():
    """Confirming that a new reservation was booked"""

    return render_template("confirmation.html")





if __name__ == "__main__":

    database_connect(app,"melonres")

    #important to disable debug later

    
    app.run(debug=True,host="0.0.0.0")
