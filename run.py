from app import app
from flask_migrate import Migrate
from app.models import db

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
