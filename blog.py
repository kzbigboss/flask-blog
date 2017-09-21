# blog.py controller

## import libraries
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g

import sqlite3

## configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '9743366228'

app = Flask(__name__)

## read in configurations
app.config.from_object(__name__)

## function for connecting to db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSOWRD']:
            error = 'Invalid credentials.  Try again.'
        else:
            session['logged in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
