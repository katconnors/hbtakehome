from model import database, User, Reservation, database_connect


def user_in_db(entered_username):
    """Check if the user is in the database"""
    return bool(User.query.filter(User.username==entered_username))


def view_own_reservations(username):
    """Users can view previous bookings"""

    own_reservations = User.query.join(Reservation).filter(User.username==username)

    return own_reservations


# def view_reservations_for_booking(date,starttime,endtime):

    


def book_reservation(date, time, reservationuser):

    reservation = Reservation(
        date=date,
        time=time,
        reservationuser = reservationuser
    )

    database.session.add(reservation)
    database.session.commit()


if __name__== "__main__":
    
    from server import app
    database_connect(app, "melonres")