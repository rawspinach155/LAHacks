# Imports
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON
import json

# Flask App
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class MedicalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(JSON)
    # Profile is a json of a dictionary of people
    diagnosis = db.Column(JSON)

    def __repr__(self) -> str:
        return f'Patient: {self.id}'@app.route("/",methods=['POST', 'GET'])
def index():

    # To gather a doctor's/patient's input
    if request.method == 'POST':
        current_data = request.form['']
        
    return render_template("index.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)