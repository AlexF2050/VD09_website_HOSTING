from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)                                           # Создаем приложение
app.config['SECRET_KEY'] = 'your_secret_key'                    # Секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clicker.db'  # Строка подключения к базе данных

db = SQLAlchemy(app)                                            # Создаем объект базы данных
bcrypt = Bcrypt(app)                                            # Создаем объект хэширования
login_manager = LoginManager(app)                               # Создаем объект логина
login_manager.login_view = 'login'                              # Устанавливаем адрес страницы логина

from app import routes, models                                  # Импортируем модули для юнит-тестирования

# Верные запросы для установки Библиотек:
# Flask
# Flask-Bcrypt
# Flask-SQLAlchemy
# Flask-Bcrypt
# Flask-Login
# Flask-WTF
