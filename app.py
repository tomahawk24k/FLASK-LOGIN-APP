from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy user
USER = {
    'username': 'admin',
    'password': 'password'
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome, {session['username']}! <a href='/logout'>Logout</a>"
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER['username'] and password == USER['password']:
            session['username'] = username
            return redirect(url_for('home'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
