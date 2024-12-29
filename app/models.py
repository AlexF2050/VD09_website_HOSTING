from app import db
from app import login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):                                      # Создание класса и модели пользователя
    id = db.Column(db.Integer, primary_key=True)                      # Идентификатор пользователя
    username = db.Column(db.String(100), unique=True, nullable=False) # Имя пользователя
    password = db.Column(db.String(200), nullable=False)              # Пароль пользователя
    clicks = db.Column(db.Integer, default=0)                         # Количество кликов

    def __repr__(self): # Вывод информации о пользователе
        return f'User {self.username} - clicks: {self.clicks}'        # Информация о пользователе

@login_manager.user_loader                                            # Загрузка пользователя из сессии
def load_user(user_id):                                               # Получение пользователя по id
    return User.query.get(int(user_id))                               # Получение пользователя по id
