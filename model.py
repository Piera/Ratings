from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import correlation

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

    def similarity(self, other):
        u_ratings = {}
        paired_ratings =[]
        for r in self.ratings:
            u_ratings[r.movie_id] = r

        for r in other.ratings:
            u_r = u_ratings.get(r.movie_id)
            if u_r:
                paired_ratings.append( (u_r.rating, r.rating) )

        if paired_ratings:
            return correlation.pearson(paired_ratings)
        else:
            return 0.0

    def predict(self, movie):
        ratings = self.ratings
        other_ratings = movie.ratings
        other_users = [ r.user for r in other_ratings ]
        similarities = [ (self.similarity(other_user), other_user) \
            for other_user in other_users ]
        similarities.sort(reverse = True)
        top_user = similarities[0]
        matched_rating = None
        for rating in other_ratings:
            if rating in other_ratings:
                if rating.user_id == top_user[1].id:
                    matched_rating = rating
                    break
        return matched_rating.rating * top_user[0]


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
    # movie = relationship("Movie", backref=backref("ratings", order_by=id))

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
