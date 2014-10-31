from flask import Flask, render_template, redirect, request
import model
import json

app = Flask(__name__)

@app.route('/')
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route('/hello', methods = ['POST'])
def hello():
    username = request.form['username']
    password = request.form['password']
    if username in model.session.query(model.User).all():
        # result = True
        return render_template("loggedin.html")
    else:
        new_user = model.User(username='username', password='password')
        model.session.add(new_user)
        model.session.commit()
        # result = False
        return render_template("newuser.html")

@app.route('/user/<int:user_id>')
def user_ratings(user_id):
    user = model.session.query(model.User).filter_by(id=user_id).one()
    # rating_list = model.session.query(model.Rating).filter_by(user_id=user_id).all()
    return render_template("ratingsbyuser.html", user = user)

@app.route('/allusers')
def allusers():
    user_list = model.session.query(model.User).all()
    return render_template("allusers.html", users=user_list)

if __name__=='__main__':
    app.run(debug = True)
