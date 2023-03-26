from flask import Flask, render_template, request, redirect, session,  flash, url_for
from flask_sqlalchemy import SQLAlchemy
import pyshorteners

app = Flask(__name__)
app.secret_key = "wasiq"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/urlshorten'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    if 'username' in session:
        return redirect('/dashboard')
    else:
        return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists!')
            return redirect(url_for('signup'))
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
        return redirect('/login')
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(
            username=username, password=password).first()
        if user is not None:
            session['username'] = username
            return redirect('/shortener')
        else:
            return render_template('index.html', error="Invalid username or password")
    else:
        return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

@app.route('/shortener', methods=['GET', 'POST'])
def shortener():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = generate_url()
        url = Url(original_url = original_url, short_url = short_url)
        db.session.add(url)
        db.session.commit()
        return render_template('dashboard.html', short_url=request.host_url+short_url)
    return render_template('dashboard.html')


@app.route('/<short_url>')
def redirect_url(short_url):
    url = Url.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

def generate_url():
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for i in range(6))


@app.route('/urls')
def urls():
    urls = Url.query.all()
    return render_template('urls.html', urls=urls)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
