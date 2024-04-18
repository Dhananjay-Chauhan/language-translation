from sqlalchemy import func
from core import app
from flask import render_template, flash, request, redirect, url_for
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
import bcrypt
 
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

from core.models.User import * 


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



    

@app.route("/")
def index():
    return render_template('base.html',title='Language Translator')


@app.route("/register" ,methods=['GET','POST'])
def register():
    if request.method == "POST":
        # print(request.form)
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone_number']
        # password = request.form['password']
        password = request.form['password']
        hash_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        user = Users(name=name, username=username,email=email,password=hash_password,phone_number=phone_number)
        db.session.add(user)
        db.session.commit() 
        
        return redirect(url_for('register'))
    
  
    return render_template('register.html')


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form['username'] 
        password = request.form['password']
        hash_password = Users.query.filter_by(username=username).first()
        print(hash_password.password.encode())
        if bcrypt.checkpw(password.encode(),hash_password.password.encode()):
            
            login_user(hash_password)
            return render_template('base.html',login_state='true')
        # else:
            


    return render_template('login.html')

# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
#     flash(f'You were successfully logged out as username : {current_user.name}')
#     logout_user()
#     return redirect(url_for('login'))


@app.get("/translate")
def translate_page():
    return render_template("translate.html")