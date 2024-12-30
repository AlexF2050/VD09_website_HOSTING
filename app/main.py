from app import app, db            # Импортируем объект приложения app и базу данных db из модуля app
from app.models import User       # Импортируем модель User из модуля models

# with app.app_context():  # После первого запуска эту строку можно удалить
#     db.create_all()  # После первого запуска эту строку можно удалить

if __name__ == '__main__':          # Проверяем, запущен ли скрипт напрямую (не импортирован)
    app.run(debug=True)             # Запускаем приложение в режиме отладки

# https://alex2050.pythonanywhere.com/