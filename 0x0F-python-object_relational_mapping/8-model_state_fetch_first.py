#!/usr/bin/python3
"""List the first states from states table in database
hbth_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_first = session.query(State).first()
    if (state_first is not None):
        print(state_first.id, state_first.name, sep=": ")
    else:
        print("Nothing")
