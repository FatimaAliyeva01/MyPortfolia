 #database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, migrate

app=Flask(__name__)
UPLOAD_FOLDER='app/static/uploads/'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
db=SQLAlchemy(app)
# migrate=Migrate(app,db)

from app.models import *
from main.routes import *
from admin.routes import *

# db.create_all()
