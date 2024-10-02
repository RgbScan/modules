from app.models import db
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user
from app.validations import RegistrationForm, LoginForm
from app.models import Users
from sqlalchemy import select

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if request.method == 'POST':
            if form.validate():
                login_or_email = form.login.data
                password = form.password.data

                user_check_login = Users.query.filter_by(login=login_or_email).first()
                user_check_email = Users.query.filter_by(email=login_or_email).first()
                if user_check_login is not None:
                    user = user_check_login
                elif user_check_email is not None:
                    user = user_check_email
                else:
                    user = None
                    flash('Пользователь с таким логином или email не найден.', 'danger')

                if user and password == user.password:
                    login_user(user, remember=form.remember_me.data)
                    flash('Вы успешно вошли!', 'success')
                    return redirect(url_for('dashboard'))  # Редирект на страницу после входа
                else:
                    flash('Неверный логин или пароль.', 'danger')

        # При GET-запросе просто рендерим шаблон с формой
        return render_template('login.html', form=form)

    @app.route('/registration', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()

        if request.method == 'POST' and form.validate():
            user_check_login = Users.query.filter_by(login=form.login.data).first()
            user_check_email = Users.query.filter_by(email=form.email.data).first()
            user = Users(form.login.data, form.email.data, form.password.data)
            try:
                if user_check_login is None and user_check_email is None:
                    db.session.add(user)
                    db.session.commit()
                    flash('Спасибо за регистрацию')
                    return redirect(url_for('login'))
                elif user_check_login is not None:
                    raise ValueError('Такой логин уже существует')
                else:
                    raise ValueError('Такая почта уже зарегистрирована')
            except Exception as e:
                db.session.rollback()  # Откат изменений в случае ошибки
                flash(str(e), 'error')  # Передача ошибки в flash
                print(f"Ошибка при сохранении пользователя: {e}")
            return redirect(url_for('login'))
        else:
            print(form.errors)  # Вывод ошибок валидации

        return render_template('form_registration.html', form=form)

    @app.route('/about')
    def about():
        return render_template('about.html')