#.
#\\
#imprt_bluprnt
#imprt_rendrtemp


from flask import Blueprint, render_template, request, flash, redirect, url_for

#model
#usr

from .models import User

from werkzeug.security import generate_password_hash, check_password_hash
#.db_imprt

from . import db
from flask_login import login_user, login_required, logout_user, current_user
#.
#auth_bluprnt

auth = Blueprint('auth', __name__)

#.
#auth_def
@auth.route('/login', methods=['GET', 'POST'])
def login():
#mthd_pst   
     if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
#usr_qury
#quryfltr
        user = User.query.filter_by(email=email).first()
        
        if user:
#if_els
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
#^
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
          
#/        
        else:
            flash('Email does not exist.', category='error')
#html
#.html_temp
    return render_template("login.html", user=current_user)


#.
#logout

@auth.route('/logout')
@login_required

#logout

def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#auth_sgnup


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
#.
#req1
        email = request.form.get('email')
        first_name = request.form.get('firstName')
#psswrd
        password1 = request.form.get('password1')
#confrm_psswrd
        password2 = request.form.get('password2')

        
#.
#email_usr
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
#len<4_error
        
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
#frst_nam<2
        
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
#.
        
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
 #,,,'

        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        #
       
       #else_nwusr 
        
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
#login_usr_tru
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

        
#retrn_rndr_temp      
    
    return render_template("sign_up.html", user=current_user)
#.
#
