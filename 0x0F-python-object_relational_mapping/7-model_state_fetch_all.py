#!/usr/bin/python3
# Lists all State objects from the database hbtn_0e_6_usa.
# Usage: ./7-model_state_fetch_all.py <mysql username> /
#                                     <mysql password> /
#
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    URL = ('mysql+mysqldb://{}:{}@localhost/{}'
           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    engine = create_engine(URL, pool_pre_ping=True)

    # Creating a Session to retrieve data from DB
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
