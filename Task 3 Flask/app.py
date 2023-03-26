from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def Home_page():
    return "Welcome to the Home page Mohammad Wasiq"


@app.route('/search')
def search_page():
    return "Welcome to Search Page Mohammad Wasiq"

@app.route('/add')
def add_fun():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))


@app.route("/uppercase")
def upper_case():
    a = request.args.get('a')
    return a.upper()


@app.route("/lowercase")
def lower_case():
    a = request.args.get('a')
    return a.lower()


if __name__ == '__main__':
    app.run(debug=True)