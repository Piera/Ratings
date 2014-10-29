from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import correlation.py

ENGINE = None
Session = None

ENGINE = create_engine("sqlite:///ratings.db", echo = False)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False)) 

Base = declarative_base()
# Base.metadata.create_all()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable = True)
    gender = Column(String(30), nullable = True)
    occupation = Column(String(20), nullable = True)
    zipcode = Column(String(15), nullable = True)
    username = Column(String(50), nullable = True)
    password = Column(String(50), nullable = True)

### Class declarations go here

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    name = Column(String(150), nullable = False)
    released_at = Column(DateTime, nullable = False)
    imdb_url = Column(String(150), nullable = True)

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer, nullable = False)

    user = relationship("User", backref=backref("ratings", order_by=id))

def create_tables():
    global ENGINE
    Base.metadata.create_all(ENGINE)


# def connect():
#     global ENGINE
#     global Session

#     ENGINE = create_engine("sqlite:///ratings.db", echo=True)
#     Session = sessionmaker(bind=ENGINE)
#     # Base.metadata.create_all()

#     return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
