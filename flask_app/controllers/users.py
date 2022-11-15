from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('loginRegister.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    data={
        'name':request.form['name'],
        'lastName':request.form['lastName'],
        'email':request.form['email'],
    }
    User.create_user(data)
    return redirect('/profilePage')

@app.route('/profilePage')
def profile():
    allUser = User.getAllUsers()
    return render_template ('profilePage.html', users = allUser)