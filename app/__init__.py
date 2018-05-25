from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "WRETRYTUY767564"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project:testpass@localhost/ims"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cdertkmvfejpom:3c7306b5777cd77c054e9c2dba2189982da36182a988ea200874d83827ac0be0@ec2-75-101-142-91.compute-1.amazonaws.com:5432/d841ef083uoabv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
