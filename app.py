from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/for_practice2'
db = SQLAlchemy(app)


class for_flask(db.Model):
    '''
    name, Id
    '''
    name = db.Column(db.String(20), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/form", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        id = request.form.get('id')
        message = request.form.get('message')
        entry = for_flask(name=name, id = id)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')


app.run(debug=True)


