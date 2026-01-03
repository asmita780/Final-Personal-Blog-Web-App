from flask import Flask, request, redirect, url_for, render_template, session as login_session, flash, Blueprint
from app.models import Post
from app import db


task_bp = Blueprint("task", __name__)

task_bp.route("/")
def home():

    username = login_session.get("username")
    if username:

        new_post = request.args.get("newpost")
        return render_template("home.html", new_post = new_post)
    
    return render_template("home.html")


@task_bp.route("/userpost", methods = ["POST", "GET"])
def userpost():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        new_post = Post(title = title, content = content)
        db.session.add(new_post)
        db.session.commit()
        flash("New post uploaded!", "seccess")
        return redirect(url_for("home", newpost=new_post))
    
    return render_template("post.html")