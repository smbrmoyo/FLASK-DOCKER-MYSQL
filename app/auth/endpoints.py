from flask import json, jsonify, flash, request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import logging

from . import auth
from .. import db
from ..models import User
from ..forms import LoginForm, SignUpForm

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('api.index'))
    form = SignUpForm()

    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('auth.login'))
        except:
            flash('There was an error creating your account', category='error')
            logging.error('There was an error creating the account')

    return render_template('sign_up.html', form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('api.index'))
    form = LoginForm()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('api.index'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        except:
            flash('There was an error logging you in', category='error')
            logging.error('There was an error logging the user in')

    return render_template('login.html', form=form)


@auth.route("/logout")
@login_required
def logout():
    try:
        logout_user()
    except:
        flash('There was an error logging you out', category='error')
        logging.error('There was an error logging the user out')

    return redirect(url_for('auth.login'))

