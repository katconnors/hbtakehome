
import os
from model import database,database_connect, User
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


if __name__ =="__main__":
    reset_melonres()
    create_test_user()