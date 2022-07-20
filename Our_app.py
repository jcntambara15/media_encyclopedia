from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt, generate_password_hash

app = Flask(__name__)
# flask_bcrypt = Bcrypt(app)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '2ef567fe4204b5cc087050a7d1f492d1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

def __repr__(self):
    return f"User('{self.username}', '{self.email}', {self.password})"

@app.route("/home_page")
def home():
    return render_template('home_page.html', subtitle='Home Page', text='You are viewing our home page')

@app.route("/about")
def about():
    return render_template('about.html', subtitle='About Page', text='We Media Encyclopedia(The Dream Team)')

@app.route("/sign_in")
def sign_in():
    return render_template('sign_in.html', subtitle='Sign In Page', text='You can sign in here!')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
        flash(f'Account created for {form.username.data}!, go to Sign In page to log in', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")