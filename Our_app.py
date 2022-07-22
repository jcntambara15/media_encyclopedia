from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt, generate_password_hash

app = Flask(__name__)
# flask_bcrypt = Bcrypt(app)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '2ef567fe4204b5cc087050a7d1f492d1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    searcher = db.Column(db.String(20), unique=True, nullable=False)

def __repr__(self):
   return f"User('{self.searcher}')"


   return f"User('{self.username}', '{self.email}')"
    
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html') 


@app.route("/about")
def about():
    return render_template('about.html', subtitle='About Page', text='You are viewing our about page')

@app.route("/search")
def search():
    return render_template('search.html', subtitle='Search Page', text='We are Media Encyclopedia(The Dream Team)')

@app.route("/find")
def find():
    return render_template('find.html', subtitle='Search Page', text='Please choose the media genre and proceed to search')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
