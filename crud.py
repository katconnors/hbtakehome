from model import database, User, Reservation, database_connect
import datetime


def user_in_db(entered_username):
    """Check if the user is in the database"""
    return bool(User.query.filter(User.username==entered_username))


def view_own_reservations(username):
    """Users can view previous bookings"""
    

    own_reservations = User.query.join(Reservation).filter(User.username==username)

    return own_reservations


def view_reservations_for_booking(date,starttime,endtime):



    time_delt = datetime.timedelta( minutes = 30)

    if not starttime:
        starttime = "10:00"
      

    start_date_object = datetime.datetime.strptime(f"{date}, {starttime}", "%Y-%m-%d, %H:%M")
                                              
    if not endtime:
        endtime = "15:00"
        
  
    end_date_object = datetime.datetime.strptime(f"{date}, {endtime}", "%Y-%m-%d, %H:%M")
        

    all_times = []

    i = start_date_object
    while i < end_date_object:
        all_times.append(i.time())
        i += time_delt


    unavailable_on_day = Reservation.query.filter(Reservation.date==date,Reservation.time>starttime,Reservation.time<endtime)
    times_unavail = [x.time for x in unavailable_on_day]
    times_unavail = set(times_unavail)
    
    all_times= set(all_times)
    
    available_reservations = all_times - times_unavail

    return sorted(available_reservations)


    
def check_against_all_reservations(date,time):
    return bool(Reservation.query.filter(Reservation.date==date,Reservation.time==time))

# prevent double booking for same day
# def check_against_own_res(date,username):

#     view_own_reservations(username)


def book_reservation(date, time, reservationuser):

    # include a conditional for opening hours

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