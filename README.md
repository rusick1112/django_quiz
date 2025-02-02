# QuizCraft
[![Python version](https://img.shields.io/static/v1?label=Python&logo=python&message=3.12.7&color=blue)](https://www.python.org/)
[![Python web framework](https://img.shields.io/static/v1?label=Django&logo=django&message=5.0.6&color=blue)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/static/v1?label=Bootstrap&logo=bootstrap&message=5.3.2&color=purple)](https://getbootstrap.com/)


## QuizApp
Данный проект представляет собой курсовую работу по теме: "**Создание веб-приложения для проведения онлайн-опросов и анкетирования**". Проект создан с помощью Django Framework, при использовании REST архитерктуры построения приложения, Bootstrap и JQuery.это удобное веб-приложение для проведения онлайн-опросов и анкетирования. Оно разработано для проверки знаний школьников и всех, кто хочет освежить свои знания в различных областях. 📝
---

## Описание проекта
Цель проекта — разработка веб-приложения, которое предлагает простые тесты, основанные на материалах школьной программы для 9-х классов. Оно будет полезно как школьникам для подготовки к контрольным работам, так и взрослым, желающим проверить уровень своих знаний.

---

## Основные возможности

- **Проведение онлайн-опросов и анкетирования** по школьным предметам. ✅
- **Интуитивно понятный интерфейс** для пользователей разного возраста. 👩‍🎓🧑‍💻
- **Автоматическая проверка ответов** с предоставлением результатов в режиме реального времени. ⚡
- **Гибкая система управления тестами** для преподавателей и администраторов. 🔧

---

## Используемые технологии

- **Язык программирования:** Python 🐍
- **Фреймворк:** Django Framework 🌐
- **База данных:** SQLite (с возможностью перехода на другие СУБД) 🗂️

### Обоснование стека

**Полнота:** встроенная админ-панель, ORM для работы с базами данных и готовая конфигурация проекта.
**Быстрая разработка:** следование принципу DRY (Don't Repeat Yourself) ускоряет процесс разработки и упрощает поддержку кода.
**Гибкость:** структура проекта упрощает организацию кода и масштабирование приложения. 📏


---

## ⚙️ Установка и запуск

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/your-repo/survey-web-app.git
cd survey-web-app
```

### 2️⃣ Настройка виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
# или
venv\Scripts\activate    # Для Windows
```

### 3️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4️⃣ Миграция базы данных

```bash
python manage.py migrate
```

### 5️⃣ Запуск сервера разработки

```bash
python manage.py runserver
```

Приложение будет доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) и [http://localhost:8000/](http://localhost:8000/) 🌍

---

