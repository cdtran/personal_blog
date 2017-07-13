from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html', page='home')


@app.route('/about')
def about():
    return render_template('about.html', page='about')


@app.route('/contact')
def contact():
    return render_template('contact.html', page='contact')
