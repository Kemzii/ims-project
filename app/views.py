"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, random, uuid, psycopg2
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm, RegisterForm
from models import Users


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
       
        username=form.username.data
        password=form.password.data
        # Get the username and password values from the form.

        # using your model, query database for a user based on the username
        # and password submitted
        # store the result of that query to a `user` variable so it can be
        # passed to the login_user() method.
        user = Users.query.filter_by(username=username).first()
        
        if user is not None and check_password_hash(user.password, password):
            # If the user is not blank, meaning if a user was actually found,
            # then login the user and create the user session.
            # user should be an instance of your `User` class
            login_user(user)

        # remember to flash a message to the user
        flash('Logged in successfully.', 'success')
        return redirect(url_for("profile"))  
    return render_template("login.html", form=form)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
###
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Render website's signup page."""
    myform = RegisterForm()
    
    if request.method == 'POST':
        if myform.validate_on_submit():
        
            firstname = myform.firstname.data
            lastname = myform.lastname.data
            email = myform.email.data
            username = myform.username.data
            trn = myform.trn.data
            gender = myform.gender.data
            password = myform.password.data
            
            id = random.getrandbits(16)
            
            db.create_all()
        
            new_user = Users(id=id, firstname=firstname, lastname=lastname, username=username, password=password, email=email, trn=trn, gender=gender)
            db.session.add(new_user)
            db.session.commit()
            
            flash('Profile successfully created!', 'success')
            return redirect(url_for("profile"))

        flash_errors(myform)
    return render_template('signup.html', form=myform)
    
    
@app.route('/createapplication', methods=["GET", "POST"])
def createapplication():
    """Render website's application page."""
    return render_template('createapplication.html')

@app.route('/life', methods=["GET", "POST"])
def life():
    """Render website's life insurance application page."""
    return render_template('life.html')

@app.route('/vehicle', methods=["GET", "POST"])
def vehicle():
    """Render website's vehicle insurance application page."""
    return render_template('vehicle.html')

@app.route('/house', methods=["GET", "POST"])
def house():
    """Render website's house insurance application page."""
    return render_template('house.html')

@app.route('/profile')
@login_required
def profile():
    """Render website's vehicle insurance application page."""
    
    
    return render_template('profile.html')



# The functions below should be applicable to all Flask apps.
###

@app.route("/logout/")
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'success')
    return render_template('home.html')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
