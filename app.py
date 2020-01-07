from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)


ENV = "prod"
# dev
if ENV == "dev":
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/tesla"
# production
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vrjsbbeqcqxuxu:a10ddd4ec346336edf119d4e15e41498f98ba605127dd32451e38a4a4efeb3b7@ec2-174-129-208-118.compute-1.amazonaws.com:5432/d7iofepg0bgigo"

# remove warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create database object
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    customer=  db.Column(db.String(200), unique = True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        customer = request.form["customer"]
        dealer = request.form["dealer"]
        rating = request.form["rating"]
        comments = request.form["comments"]
        # print(customer,dealer,rating,comments)
        # Form validation
        if customer == "" or dealer == "":
            return render_template("index.html",message="Please enter your info")
        # check if customer submits multiple feedback
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template("success.html")
        return render_template("index.html",message="You have already submitted feedback")

if __name__ == "__main__":
    app.run()