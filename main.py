from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/ahah')
def ahah():
    return render_template('ahah.html')

if __name__ == '__main__':
    app.run()