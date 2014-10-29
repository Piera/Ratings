from flask import Flask, render_template, redirect, request
import model
import json

app = Flask(__name__)

@app.route('/')
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

# @app.route('/api/judgment/user_login')

    # Put routes here to handle username and password coming in from the form
    # We can create another file to handle the function definitions if we want to!
    # When we write the login function, we need to return true/false.



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












    # result = check_DB_for_user()
    # return _convert_to_JSON(result)


if __name__=='__main__':
    app.run(debug = True)


# def _convert_to_JSON(result):
#     response = make_response(json.dumps(result))
#     response.headers['Access-Control-Allow-Origin'] = "*"
#     response.mimtype = "application/json"
