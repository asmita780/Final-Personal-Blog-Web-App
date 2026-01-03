from flask import Flask, request, render_template, redirect, url_for, session as login_session, flash,Blueprint, current_app
from app.models import UserInfo
from app import db
from werkzeug.utils import secure_filename
import os

allowed_expentions = {"png", "jpg", "jpeg", "gif"}

def allow_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in allowed_expentions


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user_exist = UserInfo.query.filter_by(email = email, password = password)
        if user_exist:
            login_session["username"] = user_exist.name
            flash(f"{user_exist.name} You have login sucessfuly!", "success")
            return redirect(url_for("home"))
        flash("Invalid email, password!", "alert")
        return render_template("login.html")
    
    return render_template("login.html")

@auth_bp.route("/logout", methods = ["POST", "GET"])
def logout():
    user = login_session.get("username")
    if user:
        login_session.pop("username")
        flash("Logged out successfuly!", "success")
        return(redirect(url_for("home")))
    
    return redirect(url_for("login"))
    
    

@auth_bp.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        userdetail = UserInfo.query.all()
        if userdetail.name != name:
            if userdetail.email != email:   
                
                append_userdata = UserInfo(name = name, email = email, password = password, filename = 'app/static/images/logo.png' )
                db.session.add(append_userdata)
                db.session.commit()
                login_session["username"] = name
                flash("Regiser successful!", "success")
                return redirect(url_for("home"))
            
            else:  
                flash("Email alredy exist.choose another!", "alert")
                return render_template("register.html")
        else:   
            flash("user name alredy exists.choose another one!", "alert")
            return render_template("register.html")

        
    return render_template("register.html")


@auth_bp.route("/account", methods = ["POST", "GET"])
def account():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        current_user = login_session.get("username")
        userdetail = UserInfo.query.filter_by(name = current_user).first()

        file = request.form.get("file")
        
        if file or file.filename !="":
            if allow_file:
                filename = secure_filename(file.filename)
                filepath = os.path.join(current_app.config["UPLOAD_FOLDER"],filename)
                file.save(filepath)
                userdetail.filename = filename

            else:
                flash("Invalid file", "alert")
                return render_template("account.html")
        
        userdetail.name = name
        userdetail.email = email
        db.session.commit()

        flash("Account updated successfuly!", "success")
        return render_template("account.html")

    return render_template("account.html")