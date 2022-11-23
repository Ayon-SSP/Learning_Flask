# Learning_Flask
Time to Learn Flask 🌶️

**Basic Code**
```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
```
```css
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

**For db connection**
```python
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# for postgresql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/db_name' 

# for mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'  
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/my_db'  


db = SQLAlchemy(app)
```

**if Using sqlite**
```python
# run in the terminal
$ python
>>> from app import db
>>> db.create_all()
```

![db done img](Resources/Img/dbCreated.jpg)


**Clear Understanding**
```python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

admin = User('admin', 'admin@example.com')

db.create_all() # In case user table doesn't exists already. Else remove it.    

db.session.add(admin)

db.session.commit() # This is needed to write the changes to database

User.query.all()

User.query.filter_by(username='admin').first()

```