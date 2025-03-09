Ось більш красива, детальна та структурована версія вашого тексту у форматі Markdown:

---

# Генератор QR-кодів

Ласкаво просимо до документації нашого проекту — інноваційного генератора QR-кодів, який поєднує простоту використання з широкими можливостями кастомізації. Цей проект створений командою ентузіастів, які прагнули розробити зручний інструмент для генерації QR-кодів із підтримкою різних планів підписки та інтуїтивним інтерфейсом.

---

## Список учасників команди

Наша команда складається з талановитих розробників, кожен із яких зробив свій внесок у створення цього проекту:

- **Артем Власов (Team Lead)**  
  - Роль: Керівник команди, координатор розробки, фронтенд-розробник, дизайнер інтерфейсу.  
  - Профіль: [GitHub - ArtemVlasov2009](https://github.com/ArtemVlasov2009)  
  - Відповідальний за архітектуру проекту та основний функціонал.

- **Ткач Богдан**  
  - Роль: Бекенд-розробник, спеціаліст із баз даних.  
  - Профіль: [GitHub - Bogdantkach12](https://github.com/Bogdantkach12)  
  - Налаштував роботу з базою даних та логіку генерації QR-кодів.

- **Іван Єжов**  
  - Роль: Фронтенд-розробник, дизайнер інтерфейсу.  
  - Профіль: [GitHub - EzhovIvan](https://github.com/EzhovIvan)  
  - Розробив стильний та зручний дизайн сторінок.

---

## Що робить наш проект

### Основна ідея

**Наш проект — це гнучкий генератор QR-кодів**, який дозволяє користувачам створювати унікальні QR-коди з різними параметрами та стилями. Ми розробили інструмент, який підходить як для простих задач (наприклад, створення QR-коду для посилання), так і для більш складних сценаріїв із кастомізацією дизайну та підтримкою платних підписок.

### Ключові можливості

- **Генерація QR-кодів**: Створюйте QR-коди для посилань, тексту чи інших даних.  
- **Кастомізація**: Налаштовуйте розмір, кольори, форму та навіть додавайте логотипи чи градієнти.  
- **Плани підписки**: Доступні різні рівні — Free, Standard, Pro та Desktop — із різними лімітами та функціями.  
- **Реєстрація та авторизація**: Захищений доступ до персоналізованих функцій.  
- **Історія генерацій**: Переглядайте та керуйте створеними QR-кодами.

---

## Технології, які ми використовуємо

Для створення цього проекту ми застосували сучасний стек технологій, що забезпечує стабільність, швидкість і зручність розробки:

- **Django**  
  - **Опис**: Потужний Python-фреймворк для веб-розробки.  
  - **Використання**: Служить основою проекту, відповідає за маршрутизацію, логіку та рендеринг сторінок.

- **SQLite3**  
  - **Опис**: Легка реляційна база даних, вбудована в Python.  
  - **Використання**: Зберігає дані користувачів, підписки та історію QR-кодів у компактному файлі.

- **Requests**  
  - **Опис**: Бібліотека для роботи з HTTP-запитами.  
  - **Використання**: Обробляє зовнішні запити, наприклад, для перевірки посилань.

- **GitHub**  
  - **Опис**: Платформа для контролю версій і спільної роботи.  
  - **Використання**: Ми використовували GitHub для зберігання коду, відстеження змін і командної співпраці.

- **PIL (Python Imaging Library)**  
  - **Опис**: Бібліотека для роботи із зображеннями.  
  - **Використання**: Генерує та редагує QR-коди, додає стилі та логотипи.

- **HTML, CSS, JavaScript**  
  - **Опис**: Базові технології веб-розробки.  
  - **Використання**:  
    - **HTML**: Структура сторінок.  
    - **CSS**: Стилізація інтерфейсу для привабливого вигляду.  
    - **JavaScript**: Динамічні елементи, наприклад, показ/приховування опцій градієнту.

---

Цей набір технологій дозволив нам створити швидкий, надійний і користувацьки орієнтований продукт. Кожен учасник команди вніс свою експертизу, щоб зробити проект максимально функціональним і зручним.

![FigJam](https://raw.githubusercontent.com/ArtemVlasov2009/DJANGO_QRCODE_GENERATOR/main/img_figjam/FigJam.png)
---

# Як запустити проект

## Локально на комп’ютері

1. **Відкрийте проект у IDE**  
   Завантажте проект із вашого репозиторію або розпакуйте його на комп’ютері. Відкрийте папку проекту у вашій інтегрованій середовищі розробки (IDE), наприклад, PyCharm, VS Code або іншій.

2. **Встановіть необхідні модулі**  
   Переконайтеся, що у вас встановлено Python. У терміналі IDE виконайте команду для встановлення всіх залежностей, які вказані у файлі `requirements.txt` (якщо такий є):
   ```bash
   pip install -r requirements.txt
   ```
   Якщо список модулів наведено окремо (наприклад, у документації), встановіть їх вручну через `pip`, наприклад:
   ```bash
   pip install django requests
   ```

3. **Запустіть файл manage.py**  
   Перейдіть у терміналі до папки, де знаходиться файл `manage.py`, і виконайте команду:
   ```bash
   python manage.py runserver
   ```
   Після цього сервер запуститься локально, і ви зможете відкрити проект у браузері за адресою `http://127.0.0.1:8000` (або іншому порті, якщо він вказаний).
---
## Віддалено на сервері

1. **Використовуйте хостинг PythonAnywhere**  
   Зареєструйтесь або увійдіть на сайт [PythonAnywhere](https://www.pythonanywhere.com).

2. **Завантажте проект**  
   - Перейдіть у розділ "Files" на PythonAnywhere.  
   - Завантажте папку з вашим проектом через інтерфейс або використайте Git, якщо проект розміщено в репозиторії.

3. **Налаштуйте віртуальне оточення**  
   - У розділі "Consoles" відкрийте Bash-консоль.  
   - Створіть віртуальне оточення командою:  
     ```bash
     mkvirtualenv myenv --python=/usr/bin/python3
     ```  
   - Встановіть необхідні модулі у віртуальному оточенні:  
     ```bash
     pip install -r requirements.txt
     ```

4. **Налаштуйте веб-додаток**  
   - У розділі "Web" натисніть "Add a new web app".  
   - Виберіть "Manual configuration" та вкажіть Python-версію.  
   - У файлі конфігурації (наприклад, `wsgi.py`) вкажіть шлях до вашого проекту.  
   - Укажіть шлях до віртуального оточення в налаштуваннях.

5. **Запустіть сервер**  
   - Після збереження налаштувань натисніть "Reload" у розділі "Web". Ваш проект стане доступним за наданою PythonAnywhere URL-адресою (наприклад, `yourusername.pythonanywhere.com`).

---
## В нашому проекті є декілька окремих застосунків, а саме / Our project has several specific applications, namely:

- **base.html** - Це початкова сторінка
- **registration.html** - Це сторінка яка відповідає за реєстрацію
- **authorization.html** - Це сторінка яка відповідає за авторизацію
- **free.html**, **standart.html**, **pro.html**, **desktop.html** - Це сторінки які відповідають за генерацію кодів з різною пропискою
---

## Структура коду

### Приклад функції рендеру сторінки (`render_home`)

```python
def render_home(request):
    # Отримуємо обраний план із сесії, якщо він є
    selected_plan = request.session.get('selected_plan', None)
    
    # Перевіряємо, чи був відправлений POST-запит
    if request.method == "POST":
        selected_plan = request.POST.get("selected_plan")
        # Перевіряємо, чи обраний план є валідним
        if selected_plan in ['free', 'standard', 'pro', 'desktop']:
            # Зберігаємо план у сесії
            request.session['selected_plan'] = selected_plan
            # Перенаправляємо на сторінку авторизації
            return redirect('authorization')
    
    # Рендеримо початкову сторінку з передачею обраного плану
    return render(request, 'base.html', {'selected_plan': selected_plan})
```

---

### Приклад HTML-шаблону (`authorization.html`)

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Сторінка авторизації{% endblock %}</title>
    <!-- Підключаємо стилі -->
    <link rel="stylesheet" href="{% static 'css/authorization.css' %}">
    <!-- Іконка сайту -->
    <link rel="icon" href="{% static 'images/Logo.png' %}" type="image/png">
</head>
<body>
    {% block content %}
    <header class="header_main">
        <!-- Логотип із посиланням на головну -->
        <a class="home_url" href="{% url 'home' %}">
            <img class="Logo_img" src="{% static 'images/Logo.png' %}" alt="Logo">
        </a>
        <!-- Навігація -->
        <a href="{% url 'home' %}" class="{% if request.resolver_match.url_name == 'home' %}current-page{% endif %}">Головна</a>
        <a href="{% url 'registration' %}" class="{% if request.resolver_match.url_name == 'registration' %}current-page{% endif %}">Реєстрація</a>
        <a href="{% url 'authorization' %}" class="{% if request.resolver_match.url_name == 'authorization' %}current-page{% endif %}">Авторизація</a>
        <a href="{% url 'contacts' %}" class="{% if request.resolver_match.url_name == 'contacts' %}current-page{% endif %}">Контакти</a>
    </header>
    <div class="registration-container">
        <h1>Авторизація</h1>
        <!-- Форма авторизації -->
        <form method="POST" action="{% url 'authorization' %}">
            {% csrf_token %}
            <div class="form-group">
                <label for="name">Ім'я користувача:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="password">Пароль:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="email-confirm">Підтвердження через Email:</label>
                <input type="email" id="email-confirm" name="email-confirm" required>
                {% if user == None %}
                <p class="Proverka_login_password">Логін або пароль некоректні</p>
                {% endif %}
            </div>
            <!-- Посилання на реєстрацію -->
            <p class="Not_reg">Не маєте аккаунта? <a class="reg_reg_btn" href="{% url 'registration' %}">Зареєструйтесь</a></p>
            <button type="submit" class="register-btn">Авторизуватися</button>
        </form>
    </div>
    {% endblock %}
</body>    
</html>
```

---

### Моделі (`models.py`)

```python
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  
import time

class Subscribers(models.Model):
    # Зв’язок із моделлю User (один до одного)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscriber = models.CharField(max_length=255)  # Ім’я підписника
    qr_code_count = models.IntegerField(default=0)  # Кількість згенерованих QR-кодів
    plan = models.CharField(max_length=10, default='free')  # План підписки
    qr_code_limit = models.IntegerField(default=10)  # Ліміт QR-кодів
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Баланс користувача

    def __str__(self):
        return self.subscriber

class qr_code(models.Model):
    # Зв’язок із моделлю User (багато до одного)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)  # Назва QR-коду
    link = models.URLField(max_length=2000, default='http://127.0.0.1:8000/')  # Посилання в QR-коді
    size = models.IntegerField(default=300)  # Розмір QR-коду
    shape = models.IntegerField(default=0)  # Форма QR-коду
    custom_style = models.CharField(max_length=50, default="default")  # Стиль QR-коду
    data_create = models.DateTimeField(default=timezone.now, null=False)  # Дата створення
    expiry_date = models.FloatField(default=time.time)  # Дата закінчення дії
    image = models.CharField(max_length=500, null=True, blank=True)  # Шлях до зображення
    plan_created = models.CharField(max_length=50, default="free")  # План, за яким створено QR-код

    def __str__(self):
        return self.name or "Unnamed QR Code"
```

---

### Налаштування URL (`urls.py`)

```python
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    # Адмін-панель
    path('admin/', admin.site.urls),
    # Головна сторінка
    path('', render_home, name='home'),
    # Реєстрація
    path('registration/', render_registration, name='registration'),
    # Авторизація
    path('authorization/', render_authorization, name='authorization'),
    # Вихід із системи
    path('logout/', logout_user, name="logout"),
    # Контакти
    path('contacts/', render_contacts, name='contacts'),
    # Генератор QR-кодів
    path('generator/', render_generator, name='generator'),
    # Історія генерацій
    path('history_gen/', render_history_gen, name='history_generations'),
    # Плани підписки
    path('free/', render_free, name='free'),
    path('standart/', render_standard, name='standart'),
    path('pro/', render_pro, name='pro'),
    # Видалення QR-коду
    path('delete_qr_code/<int:qr_id>/', views.delete_qr_code, name='delete_qr_code'),
    # Вибір плану
    path('choose_plan/', choose_plan, name='choose_plan'),
    # Desktop-версія
    path('desktop/', render_desktop, name='desktop'),
    # Головна для авторизованих
    path('home_auth/', render_home_auth, name='home_auth'),
    # Сторінка прострочених QR-кодів
    path('qr-expired/', views.qr_expired, name='qr_expired'),
    # Перенаправлення за QR-кодом
    path('create_code/<int:pk>/', views.render_redirect, name='render_redirect'),
]

# Додаємо статичні файли у режимі дебагу
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### Приклад сторінки підписки (`pro.html`)

```html
{% load static %}
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сторінка генерації</title>
    <!-- Підключаємо стилі -->
    <link rel="stylesheet" href="{% static 'css/pro.css' %}">
    <!-- Іконка сайту -->
    <link rel="icon" href="{% static 'images/Logo.png' %}" type="image/png">
</head>
<body>
    <header class="header_main">
        <!-- Логотип із посиланням -->
        <a class='home_url' href="http://127.0.0.1:8000/home_auth">
            <img class="Logo_img" src="{% static 'images/Logo.png' %}" alt="Logo" />
        </a>
        <!-- Навігація -->
        <a href="http://127.0.0.1:8000/home_auth" class="{% if request.path == '/' %}current-page{% endif %}">Головна</a>
        <a href="{% url 'generator' %}" class="{% if request.path == '/generator/' %}current-page{% endif %}">Кодогенерація</a>
        <a href="{% url 'history_generations' %}" class="{% if request.path == '/history_generations/' %}current-page{% endif %}">Генерації</a>
        <a href="{% url 'contacts' %}" class="{% if request.path == '/contacts/' %}current-page{% endif %}">Контакти</a>
        <!-- Кнопка виходу -->
        <div class="logout">
            <a class="logout_кнопка" href="{% url 'logout' %}">Вийти: {{ request.user.username }}</a>
        </div>
    </header>
    <div class="Generator_frame">
        <div class="Generator_header">
            <p>Згенеруйте ваш QR code</p>
        </div>
        <div class="Generator_internal_frame">
            <!-- Форма для генерації -->
            <form method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                <label for="name">Ім'я:</label>
                <input type="text" id="name" name="name" required><br><br>
                <label for="link_or_text">Посилання або текст:</label>
                <input type="text" id="link_or_text" name="link_or_text" required><br><br>
                <label for="size">Розмір генерації QR-коду:</label>
                <select id="size" name="size">
                    <option value="200">200x200</option>
                    <option value="300">300x300</option>
                    <option value="400">400x400</option>
                    <option value="500">500x500</option>
                </select><br><br>
                <label for="qr_color">Колір QR-коду:</label>
                <input type="color" id="qr_color" name="qr_color" value="#000000"><br><br>
                <label for="bg_color">Колір фону:</label>
                <input type="color" id="bg_color" name="bg_color" value="#FFFFFF"><br><br>
                <label for="logo">Додати логотип:</label>
                <input type="file" id="logo" name="logo" accept="image/*"><br><br>
                <label for="gradient">Налаштувати градієнт:</label>
                <input type="checkbox" id="gradient" name="gradient"><br><br>
                <!-- Налаштування градієнту -->
                <div id="gradient-colors" style="display: none;">
                    <label for="color1">Колір 1 градієнту:</label>
                    <input type="color" id="color1" name="color1" value="#ff0000"><br><br>
                    <label for="color2">Колір 2 градієнту:</label>
                    <input type="color" id="color2" name="color2" value="#00ff00"><br><br>
                </div>
                <label for="shape">Форма QR-коду:</label><br>
                <label><input type="radio" name="shape" value="rounded" checked> З закругленими кутами</label><br>
                <label><input type="radio" name="shape" value="square"> Квадратна форма</label><br><br>
                <label for="element_shape">Форма елементів QR-коду:</label><br>
                <label><input type="radio" name="element_shape" value="circle" checked> Кружки</label><br>
                <label><input type="radio" name="element_shape" value="triangle"> Трикутники</label><br>
                <label><input type="radio" name="element_shape" value="square"> Квадрати</label><br><br>
                <button class="Buttom_Down" type="submit">Генерувати</button>
            </form>
            <!-- Відображення QR-коду -->
            <div class="qr-code-overlay">
                <h2>Ваш QR-код:</h2>
                <div style="width: 200px; height: 200px; overflow: hidden;">
                    {% if qr_image_url %}
                        <img src="{{ qr_image_url }}" alt="QR-код" id="qr-code-img" style="width: 200px; height: 200px; object-fit: contain;">
                    {% else %}
                        <img src="{% static 'images/qrCodeExample.png' %}" alt="Placeholder" id="qr-code-placeholder" style="width: 200px; height: 200px; object-fit: contain;">
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    <!-- Скрипт для показу/приховування градієнту -->
    <script>
        document.getElementById('gradient').addEventListener('change', function() {
            const gradientColors = document.getElementById('gradient-colors');
            gradientColors.style.display = this.checked ? 'block' : 'none';
        });
    </script>
</body>
</html>
```

---

## Чому SQLite3?

- **Вбудована в Python**: не потребує додаткового встановлення.  
- **Простота**: вся база даних зберігається в одному файлі.  
- **Досвід**: ми вже працювали з SQLite3 раніше.  
- **Гнучкість**: для Flask можуть знадобитися міграції, але для базового використання достатньо одного файлу.

---

## Дизайн у Figma

Прототип дизайну доступний за посиланням:  
[Figma - QR Code Generator Project](https://www.figma.com/design/DdHVri8QFYcHu0aAtPD0YH/QR-Code-Generator-Project?node-id=223-92&t=ud8Q13eHWrrlpWDk-0)

---

## Висновки

Під час роботи над проектом ми:  
- Дізналися багато нового про розробку веб-сайтів.  
- Освоїли сучасні технології (Django, SQLite3 тощо).  
- Покращили навички командної роботи та розуміння коду.  


--- 

Сподіваюся, цей формат вам сподобається! Якщо потрібні зміни, дайте знати.

