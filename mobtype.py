from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "plasmid.db"

db = SQLAlchemy(app)

class Inctype(db.Model):
    sample_id = db.Column(db.String(30),primary_key=True)
    rep_type = db.Column(db.String(60),nullable=False)
    rep_type_accession = db.Column(db.String(60),nullable=False)
    predicted_mobility = db.Column(db.String(60),nullable=False)
    organism = db.Column(db.String(60),nullable=False)
    taxid = db.Column(db.Integer,nullable=False)
    

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True) 