import model
import csv
from datetime import datetime
# import sys

def load_users(session):
    with open('seed_data/u.user') as csvfile:
        user_file = csv.reader(csvfile, delimiter = '|')
        for users in user_file:
            id = (int(users[0]))
            age = (int(users[1]))
            gender = users[2]
            occupation = users[3]
            zipcode = users[4]
            user = model.User(id= id, age = age,\
             gender = gender.decode("latin-1"), occupation = occupation.decode(
                "latin-1"), zipcode = zipcode.decode("latin-1"))
            session.add(user)
        session.commit()
    # use u.user
    

def load_movies(session):
    with open('seed_data/u.item') as csvfile:
        movies_file = csv.reader(csvfile, delimiter = '|')
        for movie in movies_file:
            id = (int(movie[0]))
            movies = movie[1]
            released_at = movie[2]
            # released_at=released_at.strip() 
            # released_at = datetime.strptime(released_at,'%d-%b-%Y')        
            if released_at == '':
                released_at = datetime.strptime("12-Dec-1900",'%d-%b-%Y')  
            else:
                released_at = datetime.strptime(released_at,'%d-%b-%Y') 
            url = movie[3] 

            movie = model.Movie(id=id, name = movies.decode("latin-1"), \
            released_at =released_at, \
            imdb_url = url.decode("latin-1"))
            session.add(movie)
        session.commit()


def load_ratings(session):
    with open ('seed_data/u.data') as csvfile:
        ratings_file = csv.reader(csvfile, delimiter = '\t')
        for data in ratings_file:
            movie_id = int(data[0])
            user_id = int(data[1])
            movie_rating = int(data[2])
            rating = model.Rating(movie_id = movie_id, \
                user_id = user_id, rating=movie_rating)
            session.add(rating)
        session.commit()

    # use u.data

def main(session):
    # objectUsers,objectRatings,objectMovies = open(sys.argv[3])
    load_users(session)
    load_movies(session)
    load_ratings(session)



    # You'll all each of the load_* functions with the session as an argument
    
if __name__ == "__main__":
    s= model.connect()
    main(s)
