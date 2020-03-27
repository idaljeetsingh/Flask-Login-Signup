"""
    Title: Flask Login/Signup with Email-Verification
    Module Name: server
    Author: Daljeet Singh Chhabra
    Language: Python
    Date Created: 27-03-2020
    Date Modified: 27-03-2020
    Description:
        ###############################################################
        ##  Controls the endpoints of Flask Login/Signup.
        ###############################################################
"""
from flask import (Flask, render_template, g, request, redirect, session, url_for, Response)
from backend import (check_auth_login, register_auth_user, verify_usr_eml)
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return "Hello World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        redirect(url_for(index))
    else:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            if check_auth_login(request.form['usr_name'], request.form['usr_pwd']):
                session['user'] = request.form['usr_name']
                g.user = session['user']
                return redirect(url_for('index'))
            else:
                return Response("<script type='text/javascript'> alert('Failed');</script>")  # )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        if register_auth_user(usr_eml=request.form['usr_eml'], usr_fname=request.form['usr_fname'],
                              usr_lname=request.form['usr_lname'], usr_pwd=request.form['usr_pwd'],
                              usr_phone=request.form['usr_phone']):
            return Response(
                '<script type="text/javascript"> alert("Registered Successfully. Check Email for verification");</script>')
        else:
            return Response(
                f"<script type='text/javascript'>alert('Failed');</script>")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if g.user:
        g.user = None
        session.pop('user')
        session.pop('name')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/verify/<string:key>', methods=['GET'])
def verify(key):
    resp = verify_usr_eml(key)
    return Response(f'<script type="text/javascript"> alert("{resp}") </script>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
