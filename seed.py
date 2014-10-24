import model
import csv
import sys

def load_users(session):

    with open('u.user.csv') as csvfile:
        user_file = csv.reader(csvfile, delimiter = '|')
        for users in user_file:
            id = (int(users[0]))
            age = (int(users[1]))
            gender = users[2]
            occupation = users[3]
            zipcode = (int(users[4]))
            user = model.User(id= id.decode("latin-1"), age = age.decode("latin-1"), gender = gender.decode("latin-1"), occupation = occupation.decode(
                "latin-1"), zipcode = zipcode.decode("latin-1"))
            session.add(user)
        session.commit()

    # use u.user
    

def load_movies(session):
    # use u.item
    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    objectUsers,objectRatings,objectMovies = open(sys.argv[3])
    load_users(objectUsers)
    load_movies(objectMovies)
    load_ratings(objectRatings)




    # You'll all each of the load_* functions with the session as an argument
    
if __name__ == "__main__":
    s= model.connect()
    main(s)
