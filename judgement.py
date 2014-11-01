from flask import Flask, render_template, redirect, request
import model
from model import session as dbsession
import json

app = Flask(__name__)

@app.route('/')
def index():
    user_list = dbsession.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route('/login', methods = ['POST'])
def login():
    username = request.form['username']
    # password = request.form['password']
    if username in dbsession.query(model.User).filter_by(username=username).all():
        print username
        return render_template("loggedin.html")
    else:
    #     new_user = model.User(username='username', password='password')
    #     model.dbsession.add(new_user)
    #     model.dbsession.commit()
        # result = False
        return render_template("signup_form.html")

@app.route('/user/<int:user_id>')
def user_ratings(user_id):
    user = dbsession.query(model.User).filter_by(id=user_id).one()
    # rating_list = model.session.query(model.Rating).filter_by(user_id=user_id).all()
    return render_template("ratingsbyuser.html", user = user)

@app.route('/allusers')
def allusers():
    user_list = dbsession.query(model.User).all()
    return render_template("allusers.html", users=user_list)

if __name__=='__main__':
    app.run(debug = True)


# route in this file to get the user name and password
# check if they are in the database
# use session to tell browser they are logged in
