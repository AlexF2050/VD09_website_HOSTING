from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):                                                  # Создание формы регистрации
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=35)]) # Создание поля для ввода имени
    password = PasswordField('Password', validators=[DataRequired()])         # Создание поля для ввода пароля
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) # Создание поля для подтверждения пароля
    submit = SubmitField('Регистрация')                                             # Создание поля для отправки формы

    def validate_username(self, username):                                          # Валидация имени
        user = User.query.filter_by(username=username.data).first()                 # Поиск пользователя по имени
        if user:
            raise ValidationError('Такое имя уже существует')                       # юзер с таким именем уже существует

class LoginForm(FlaskForm):                                                         # Создание формы входа
    username = StringField('Username', validators=[DataRequired()])            # Создание поля для ввода имени
    password = PasswordField('Password', validators=[DataRequired()])          # Создание поля для ввода пароля
    submit = SubmitField('Вход')                                                    # Создание кнопки для отправки формы

# Верные запросы для установки Библиотек:
# Flask
# Flask-Bcrypt
# Flask-SQLAlchemy
# Flask-Bcrypt
# Flask-Login
# Flask-WTF
# Flask-Migrate