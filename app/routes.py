from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

from app import app


@app.route('/')
def index():
    return render_template("index.html", title="home")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("user name is {} and remember is ".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))

    return render_template("login.html", form=form)
