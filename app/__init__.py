from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "WRETRYTUY767564"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project:testpass@localhost/ims"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eqmpxbipctibfh:634084a3614ad74e98290588de45c31fa9d18bee8fe342021d56bfb07604ee81@ec2-23-23-130-158.compute-1.amazonaws.com:5432/dd5devc8qldbs1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
