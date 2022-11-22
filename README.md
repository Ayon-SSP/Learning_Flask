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