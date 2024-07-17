from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from bson import ObjectId
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# MongoDB configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

@app.route('/')
def index():
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashed_password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': request.form['username'], 'password': hashed_password})
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
        
        return 'That username already exists!'

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username']})

        if login_user:
            if bcrypt.checkpw(request.form['password'].encode('utf-8'), login_user['password']):
                session['username'] = request.form['username']
                return redirect(url_for('dashboard'))
        
        return 'Invalid username/password combination'

    return render_template('signin.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
