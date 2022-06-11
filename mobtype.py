from crypt import methods
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///plasmid.db"

db = SQLAlchemy(app)

class Inctype(db.Model):
    sample_id = db.Column(db.String(30),primary_key=True)
    rep_type = db.Column(db.String(60),nullable=True)
    rep_type_accession = db.Column(db.String(60),nullable=True)
    predicted_mobility = db.Column(db.String(60),nullable=False)
    organism = db.Column(db.String(60),nullable=False)
    taxid = db.Column(db.Integer,nullable=False)

class queryForm(FlaskForm):
    search = StringField('Search',validators=[DataRequired("Enter organism id please!")])
    submit = SubmitField('Submit')

@app.route("/",methods=['GET','POST'])
def home():
    form = queryForm()
    if form.validate_on_submit():
        # print(form.search.data)
        plasmid = Inctype.query.filter_by(sample_id=form.search.data).first()
        return render_template("home.html",plasmid=plasmid)
    return render_template("home.html",plasmid='',form=form)
if __name__ == "__main__":
    app.run(debug=True) 