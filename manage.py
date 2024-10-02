from flask.cli import with_appcontext

from app import db, app

@with_appcontext
def create_tables():
    """Создает все таблицы в базе данных."""
    with app.app_context():
        db.create_all()
        print("Все таблицы созданы.")
