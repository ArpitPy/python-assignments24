from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return 'That username is already taken!'
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'User registered successfully!'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['logged_in'] = True
            return 'Logged in successfully!'
        else:
            return 'Invalid username or password!'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return 'Logged out successfully!'
def login_required(func):
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            return 'You need to login first!'
    return wrapper

@app.route('/profile')
@login_required
def profile():
    return 'This is your profile page!'
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
