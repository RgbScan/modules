from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password


class Person(db.Model):
    __tablename__ = 'person'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    employee: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    users_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    def __init__(self, first_name, last_name, employee):
        self.login = first_name
        self.email = last_name
        self.password = employee
