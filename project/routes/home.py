from project import app
from flask import render_template


@app.route('/')
def show_home_page():
    # This renders them home.html from the templates directory
    return render_template('home.html')


@app.route('/about_us')
def about_us():
    # This doesn't render a template, it just returns a dumb string
    return "This is the about us page"
