from project import app
from flask import redirect, render_template, request


@app.route('/register')
def show_register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def do_register():

    # This is the most complicated function. It is what happens when you
    # click sumbit from the /register form.

    # Any form fields from a previous page can be retrieved this way
    username = request.form.get('username')

    # We can do things like check for existing users
    if username == 'kaleb':
        # Templates can be given extra data, like error (see how its used in register.html)
        # return is the last thing a function does. If it gets here, the function is over
        return render_template('register.html', error='User Exists')

    # We can continue to do more error checking and stuff
    if len(username) < 3:
        return render_template('register.html', error='Username too short')

    # If the function has not returned by now, we'll assume it is successful
    return "Registered successfully!"
