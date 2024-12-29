# Прописываем маршруты и логику работы программы

from flask import render_template, equest, redirect, url_for, flash
from app import app, db, bcrypt
from app.models import User
from app.forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')                                                     # переадресация на главную страницу
@login_required                                                     # создаём декоратор login_required
def index():                                                        # создаём функцию для авторизации пользователя
    return render_template('index.html')                            # юзер должен быть авторизован

@app.route('/register', methods=['GET', 'POST'])                    # создаём функцию для регистрации пользователя
def register():                                                     # юзер должен быть авторизован
    if current_user.is_authenticated:                               # проверка юзер уже авторизован
        return redirect(url_for('index'))                           # перенаправление на главную страницу
    form = RegistrationForm()                                       # создаём форму регистрации
    if form.validate_on_submit():                                   # проверяем нажата ли кнопка регистрации
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # шифруем пароль
        user = User(username=form.username.data, password=hashed_password) # добавляем объекты пользователя
        db.session.add(user)                                        # добавляем пользователя в базу данных
        db.session.commit()                                         # создаём транзакцию и сохраняем изменения
        flash('Вы успешно зарегистрировались!', 'success') # сообщение юзеру
        return redirect(url_for('login'))                           # перенаправление на страницу авторизации Входа
    return render_template("register.html", form=form) # переход на страницу регистрации


@app.route('/login', methods=['GET', 'POST'])                       # создаём функцию для авторизации пользователя
def login():                                                        # проверяем - юзер должен быть авторизован
    if current_user.is_authenticated:                               # Если пользователь авторизован
        return redirect(url_for('index'))                           # перенаправление на главную страницу
    form = LoginForm()                                              # создаём форму авторизации
    if form.validate_on_submit():                                   # проверяем нажата ли кнопка входа
        user = User.query.filter_by(username=form.username.data).first() # поиск пользователя по имени, если есть то сораняем в переменную user
        if user and bcrypt.check_password_hash(user.password, form.password.data): # сравниваем пароли юзера и формы в которую ввели данные
            login_user(user)                                        # юзер авторизован
            return redirect(url_for('index')) # перенаправление на главную страницу так, как юзер авторизован и найден
        else:
            flash('Неверно введены данные аккаунта', 'danger') # сообщение юзеру
    return render_template("login.html", form=form) # переход на страницу авторизации Входа

@app.route('/logout')                                               # создаём функцию для выхода из аккаунта
def logout(): #
    logout_user()
    return redirect(url_for('login'))                               # перенаправление на страницу авторизации Входа

@app.route('/click')                                                # создаём функцию для показа количества кликов
@login_required                                                     # юзер должен быть авторизован
def click():                                                        # создаём функцию для показа количества кликов
    current_user.clicks += 1                                        # юзер кликнул на ссылку
    db.session.commit()                                             # создаём транзакцию и сохраняем изменения
    return redirect(url_for('index'))                               # перенаправление на главную страницу