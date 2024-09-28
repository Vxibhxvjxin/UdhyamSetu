from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage for registered users
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # Authentication logic (in reality, use a database)
    if email in users and users[email] == password:
        return redirect(url_for('dashboard'))
    else:
        return 'Login Failed! Invalid credentials.'

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # Registration logic (in reality, save to a database)
    users[email] = password
    return redirect(url_for('sign_in'))

if __name__ == '__main__':
    app.run(debug=True)
