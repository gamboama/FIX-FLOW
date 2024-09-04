from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DB="mysql+mysqlconnector://root:2004@localhost:3306/tjt"

create = create_engine(URL_DB)

local_session = sessionmaker(autocommit=False, autoflush=False, bind=create)

base= declarative_base()

def get_db():
    connection=local_session()
    try:
        yield connection 
    finally:
        connection.close 