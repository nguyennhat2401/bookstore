from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary
from urllib.parse import quote


app=Flask(__name__)
app.secret_key='KJHKHJKYGJYGBJNMK@^*&$^*#@!#*(>?<'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/bookstore?charset=utf8mb4" % quote("240104")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE']=4


db=SQLAlchemy(app=app)
Login=LoginManager(app=app)


cloudinary.config(
    cloud_name = "dvlwb6o7e",
    api_key = "315637758944728",
    api_secret = "A34d8SUWJZnBLiGAgOPEIhqRB_c", # Click 'View API Keys' above to copy your API secret
    secure=True
)

