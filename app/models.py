from app import db
from datetime import datetime, timezone

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    filenaee  = db.Column(db.String(200), nullable = False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_ap = db.Column(db.DataTime, default = lambda: datetime.now(timezone.utc))