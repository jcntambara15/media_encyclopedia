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
def default():
    return render_template('index.html') 


@app.route("/home_page")
def home():
    return render_template('home_page.html', subtitle='Home Page', text='You are viewing our home page')

@app.route("/about")
def about():
    return render_template('about.html', subtitle='About Page', text='We are Media Encyclopedia(The Dream Team)')

@app.route("/sign_in")
def sign_in():
    return render_template('sign_in.html', subtitle='Sign In Page', text='You can sign in here!')

@app.route("/register", methods=['GET'])
def search():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        if form.validate_on_submit():
            user = User(search=form.search.data)
            db.session.add(user)
            db.session.commit()
        flash(f'Search generated for {form.search_input.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    # return render_template('register.html', title='Search', form=form)
  
        flash(f'Account created for {form.username.data}! go to Sign In page to log in', 'success')
        return redirect(url_for('home_page')) # if so - send to home page
    return render_template('register.html', title='Search', form=form)
    return render_template('register.html', title='Register', form=form)

# Route for handling the login page logic
@app.route('/sign_in', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
