from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = "dev"

if ENV == "dev":
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
else:
    app.debug = False
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgres://xfhasjzbqohpbw:a7225edd626e434811db6c973690174c9b6b19ce3570d0aa5381204683e970bc@ec2-34-204-22-76.compute-1.amazonaws.com:5432/d11cji2ktgh09v"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Kid(db.Model):
    __tablename__ = "kid"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    age = db.Column(db.Integer)

    def __init__(self, name, age, comments):
        self.name = name
        self.age = age
        self.comments = comments


class Nanny(db.Model):
    __tablename__ = "nanny"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    age = db.Column(db.Integer)
    available = db.Column(db.Boolean)

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


class Zoom(db.Model):
    __tablename__ = "zoom"
    id = db.Column(db.Integer, primary_key=True)
    kid_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    nanny_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __init__(self, kid_id, nanny_id, start_time, end_time):
        self.kid_id = kid_id
        self.nanny_id = nanny_id
        self.start_time = start_time
        self.end_time = end_time


# this kid prefers this nanny
class Preference(db.Model):
    __tablename__ = "preference"
    id = db.Column(db.Integer, primary_key=True)
    kid_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    nanny_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    score = db.Column(db.Integer)

    def __init__(self, kid_id, nanny_id):
        self.kid_id = kid_id
        self.nanny_id = nanny_id
        self.score = score


@app.route("/")
def index():
    return render_template("index.html")


# @app.route('someroute', methods=['POST/GET/DELETE'])
# def somefunction


if __name__ == "__main__":
    app.run()
