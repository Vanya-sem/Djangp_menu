# Создание проекта Меню


## Установка

1. Клонирование репозитория 

```git clone https://github.com/Vanya-sem/Django_menu```

2. Переход в директорию проекта

```cd Test_Project```

3. Создание виртуального окружения

```python -m venv venv```

4. Активация виртуального окружения

```venv/Scripts/activate```

5. Установка зависимостей

```pip install -r requirements.txt```

6. Создание суперпользователя

```python manage.py createsuperuser```

7. Миграции

```python manage.py migrate```

8. Запуск

```python manage.py runserver```


Готово! Теперь все пункты меню, созданные через стандартное приложение админки Django будут отображаться с корректными ссылками.

## Комментарий разработчика
Древовидное меню реализовано с помощью шаблонных тегов.
Все требования были выполнены.

Хотелось конечно еще добавить стиля с помощью CSS и JS (взяв предварительно шаблон),
однако что то сильно пошло не так)). Прошу не судить строго и приветствую адекватную критику.
