from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Tools to use the Database, using objects Python
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:15Anderson12albukerk95@localhost/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)
migrate = Migrate(app, database)

from app.controllers import routes
