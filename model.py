from flask_sqlalchemy import SQLAlchemy


database= SQLAlchemy()


#sql-alchemy 1 lecture

def database_connect(app,database_name):

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{database_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    

    database.app = app
    database.init_app(app)


class User(database.Model):

    """Site users"""

    __tablename__ = "users"

    id = database.Column(database.Integer, primary_key = True, autoincrement = True)
    username = database.Column(database.Text, nullable= False)
    

    reserved = database.relationship('Reservation', back_populates="user")

    def __repr__(self):
        return f"<id={self.id} username= {self.username}>"
    


class Reservation(database.Model):

    """Melon tasting reservations that have been booked"""

    __tablename__ = "reservations"

    id = database.Column(database.Integer, primary_key = True, autoincrement = True)
    date = database.Column(database.Date, nullable= False)
    time = database.Column(database.Time, nullable= False)
    reservationuser = database.Column(database.Integer, database.ForeignKey('users.id'))
    

    user = database.relationship('User', back_populates="reserved")


    def __repr__(self):
        return f"<id={self.id} date= {self.date} time= {self.time} reservationuser= {self.reservationuser}>"
    


if __name__== "__main__":

    from server import app
    database_connect(app, "melonres")
