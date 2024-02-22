
import os
from model import database,database_connect, User, Reservation
import server

#will drop the db


def reset_melonres():

    os.system("dropdb melonres")
    os.system("createdb melonres")


    database_connect(server.app,"melonres")

    database.create_all()


def create_test_user():
    """Test user to check functionality"""

    testuser= User(username="testuser")

    database.session.add(testuser)
    database.session.commit()


def create_test_res():
    """Test reservation to check functionality"""

    testres = Reservation(date="2024-02-23", time="10:30", reservationuser= 1)

    database.session.add(testres)
    database.session.commit()




if __name__ =="__main__":
    reset_melonres()
    create_test_user()
    create_test_res()