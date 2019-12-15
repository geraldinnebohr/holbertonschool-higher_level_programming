#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    mysql_state = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_user, mysql_passwd, mysql_db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    match = None
    for state in session.query(State).filter(State.name == mysql_state).all():
        match = state.id
    if match:
        print(match)
    else:
        print('Not found')
    session.close()
