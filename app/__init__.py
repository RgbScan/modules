from flask import Flask
from app.models import db
from flask_wtf import CSRFProtect
from app.routes import init_routes


app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = 'your_secret_key_here'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/data.db'
db.init_app(app)
init_routes(app)
