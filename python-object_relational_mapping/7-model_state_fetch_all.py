#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

# imports from sqlalchemy and model_state
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    """main function to list all State objects from the database hbtn_0e_6_usa"""

    # create engine and session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all State objects and print their id and name
    states = session.query(State).order_by(State.id).all()

    # print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()