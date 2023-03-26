from flask import Flask, render_template, request, redirect, session,  flash, url_for
from flask_sqlalchemy import SQLAlchemy
import pyshorteners

app = Flask(__name__)
app.secret_key = "wasiq"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/urlshort'
db = SQLAlchemy(app)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(50), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/shortener', methods=['GET', 'POST'])
def shortener():
    original_url = request.form['url']
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(original_url)
    url = Url(original_url=original_url, short_url=short_url)
    db.session.add(url)
    db.session.commit()
        # generate shortened URL and display it to user
    return render_template('index.html', short_url=short_url)

@app.route('/urls')
def urls():
    urls = Url.query.all()
    return render_template('urls.html', urls=urls)


if __name__ == '__main__':
    app.run(debug=True)
