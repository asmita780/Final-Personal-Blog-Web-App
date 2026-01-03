from flask import Flask, request, render_template, redirect, url_for, session as login_session, flash,Blueprint
from app.models import UserInfo
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user_exist = UserInfo.query.filter_by(email = email, password = password)
        if user_exist:
            login_session["email"] = user_exist.email
            flash(f"{user_exist.name} You have login sucessfuly!", "success")
            return redirect(url_for("home"))
        flash("Invalid email, password!", "alert")
        return render_template("login.html")
    return render_template("login.html")

