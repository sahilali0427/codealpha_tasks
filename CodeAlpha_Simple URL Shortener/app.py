from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'

db = SQLAlchemy(app)

# Table
class Urls(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    original_url = db.Column(db.String(500))

    short_code = db.Column(db.String(10), unique=True)


# Home page
@app.route('/')
def home():

    return render_template("index.html")


# Generate short code
def generate_code():

    letters = string.ascii_letters

    numbers = string.digits

    all_characters = letters + numbers

    code = ""

    for i in range(6):

        code += random.choice(all_characters)

    return code


# Shorten URL
@app.route('/shorten', methods=['POST'])
def shorten():

    long_url = request.form['long_url']

    short_code = generate_code()

    # Save in database
    new_link = Urls(
        original_url=long_url,
        short_code=short_code
    )

    db.session.add(new_link)

    db.session.commit()

    # Better URL format
    short_url = request.host_url + "u/" + short_code

    return render_template(
        "index.html",
        short_url=short_url
    )


# Redirect
@app.route('/u/<code>')
def redirect_url(code):

    data = Urls.query.filter_by(short_code=code).first()

    if data:

        return redirect(data.original_url)

    else:

        return "Link Not Found"


# Run app
if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(debug=True)