# Import: pip install flask
from flask import Flask, render_template

app = Flask(__name__)


# Making A Home Route
@app.route('/')
def index():
    # Returning A HTML File
    return render_template('index.html')

# Making A User Route
@app.route('/<user>')
# Making Function And Adding Te User Varuable
def route2(user):
    # Checking If The User Is Equal To Something
    if user.lower() == "github":
        # If It Is, Returng The User.html File
        return render_template('user.html')
    else:
        # If Not, Just Printing Out Not A User
        return f"""<h1> Not A User </h1>"""

@app.route('/<user>/<password>')
def route3(user, password):
    # Adding More Security Values
    if user.lower() == "gtihub" and password.lower() == "coding":
        return render_template("admin.html")
    else:
        return f"""<h1> Not A User </h1>"""

@app.route('/var')
def var():
    value = "GitHub Projects"
    return render_template('var.html', value=value)
