#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""

from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for obj in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(obj[0] + ": (" + str(obj[1]) + ") " + obj[2])
