from app import app, db            # Импортируем объект приложения app и базу данных db из модуля app
from app.models import User        # Импортируем модель User из модуля models

if __name__ == '__main__':          # Проверяем, запущен ли скрипт напрямую (не импортирован)
    app.run(debug=True)             # Запускаем приложение в режиме отладки