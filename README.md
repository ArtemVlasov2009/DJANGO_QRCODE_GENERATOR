# Генератор QR-кодів

## Мета створення проєкту та його користь для користувача

**Генератор QR-кодів** — це інноваційний веб-додаток, створений для спрощення процесу генерації QR-кодів із широкими можливостями кастомізації. Наша мета — надати користувачам простий, інтуїтивний і водночас потужний інструмент для створення унікальних QR-кодів, які можна адаптувати під різні потреби: від простих посилань до складних дизайнів із логотипами та градієнтами.

Цей інструмент дозволяє користувачам налаштовувати кольори, форми та стилі QR-кодів, щоб вони ідеально вписувалися в дизайн бренду або особистий стиль. Ви можете додавати логотипи, змінювати фонові кольори та навіть створювати анімовані QR-коди для більш привабливого візуального ефекту.

Проєкт корисний для:

- **Індивідуальних користувачів**: швидко створювати QR-коди для особистих посилань чи тексту.
- **Бізнесу**: генерувати брендовані QR-коди з логотипами та унікальним дизайном для маркетингу.
- **Розробників**: досліджувати приклад реалізації веб-додатку на Django з інтеграцією бази даних і кастомізацією.
- **Освітніх закладів**: створювати QR-коди для навчальних матеріалів, посилань на ресурси та інтерактивних завдань.
- **Медичних установ**: використовувати для швидкого доступу до інформації про пацієнтів або медичних записів.
- **Логістичних компаній**: спрощувати процес відстеження посилок та управління запасами.
- **Ресторанів та кафе**: надавати клієнтам доступ до меню, акцій та відгуків через QR-коди.
- **Маркетологів**: аналізувати ефективність рекламних кампаній за допомогою QR-кодів.
- **Видавництв**: інтегрувати QR-коди в друковані матеріали для швидкого доступу до додаткової інформації.

Завдяки гнучким планам підписки (Free, Standard, Pro, Desktop) користувачі можуть обрати функціонал, який відповідає їхнім потребам, від базового до професійного рівня.

---

## План-навігація по README

1. [Назва проєкту](#генератор-qr-кодів)  
2. [Мета створення проєкту та його користь](#мета-створення-проєкту-та-його-користь-для-користувача)  
3. [План-навігація по README](#план-навігація-по-readme)  
4. [Склад команди розробників](#склад-команди-розробників)  
5. [Посилання на Figma-дизайн та FigJam](#посилання-на-figma-дизайн-та-figjam)  
6. [Структура проєкту](#структура-проєкту)  
7. [Детальна специфікація застосунків](#детальна-специфікація-застосунків)  
8. [Як запустити проєкт](#як-запустити-проєкт)  
9. [Висновки](#висновки)  

---

## Склад команди розробників

Наша команда складається з трьох талановитих учасників, кожен з яких вносить унікальний внесок у проєкт.

*   **Артем Власов**
    *   **Роль:** Керівник команди, фронтенд-розробник, дизайнер інтерфейсу.
    *   **GitHub:** [ArtemVlasov2009](https://github.com/ArtemVlasov2009/DJANGO_QRCODE_GENERATOR)
    *   **Відповідальність:** Архітектура проєкту, дизайн, основний функціонал.
*   **Ткач Богдан**
    *   **Роль:** Бекенд-розробник, спеціаліст із баз даних.
    *   **GitHub:** [Bogdantkach12](https://github.com/Bogdantkach12/Qr_code_generator)
    *   **Відповідальність:** Логіка генерації QR-кодів, робота з базою даних SQLite3.
*   **Іван Єжов**
    *   **Роль:** Фронтенд-розробник, дизайнер інтерфейсу.
    *   **GitHub:** [EzhovIvan](https://github.com/EzhovIvan)
    *   **Відповідальність:** Стильний дизайн сторінок, інтерактивні елементи.

---

## Посилання на Figma-дизайн та FigJam

- **Figma-дизайн**:  
  [Figma - QR Code Generator Project](https://www.figma.com/design/DdHVri8QFYcHu0aAtPD0YH/QR-Code-Generator-Project?node-id=223-92&t=ud8Q13eHWrrlpWDk-0)  
  Прототип дизайну інтерфейсу, який відображає структуру та стиль сторінок.  

- **FigJam**:  
  ![Схема FigJam](https://raw.githubusercontent.com/ArtemVlasov2009/DJANGO_QRCODE_GENERATOR/main/img_figjam/FigJam.png)  
  Схема планування проєкту, яка допомогла нам організувати задачі та ідеї.  

---

## Структура проєкту

Проєкт побудований на фреймворку **Django** і складається з кількох ключових компонентів:
- **`main/`**: базовий додаток.  
- **`manage.py`**: основний файл для запуску серверу та управління проєктом.  
- **`home/views.py`**: логіка відображення сторінок і обробки запитів.  
- **`home/models.py`**: моделі даних для користувачів і QR-кодів.  
- **`home/urls.py`**: маршрутизація URL-адрес.  
- **`templates/`**: HTML-шаблони для сторінок (base.html, registration.html тощо).  
- **`static/`**: статичні файли (CSS, JS, зображення).  
- **`media/`**: збережені зображення QR-кодів.  
- **`db.sqlite3`**: база даних проєкту.  

---

## Детальна специфікація застосунків

Нижче описано кожен застосунок проєкту, його призначення, особливості та приклади коду.

### 1. `base.html` — Початкова сторінка
- **Мета**: Вітальна сторінка, яка знайомить користувача з проєктом і пропонує обрати план підписки.  
- **Особливості**:  
  - Вибір плану (Free, Standard, Pro, Desktop) через POST-запит.  
  - Перенаправлення на авторизацію після вибору.  
- **Приклад коду** (логіка у `views.py`):  
  ```python
  def render_home(request):
      selected_plan = request.session.get('selected_plan', None)
      if request.method == "POST":
          selected_plan = request.POST.get("selected_plan")
          if selected_plan in ['free', 'standard', 'pro', 'desktop']:
              request.session['selected_plan'] = selected_plan
              return redirect('authorization')
      return render(request, 'base.html', {'selected_plan': selected_plan})
  ```

### 2. `registration.html` — Реєстрація
- **Мета**: Дозволяє новим користувачам створити акаунт.  
- **Особливості**:  
  - Форма із полями для імені, пароля та email.  
  - Перевірка унікальності імені та збереження в базі даних.  
- **Унікальна механіка**: Реєстрація пов’язана з моделлю `Subscribers`, яка відстежує підписку та ліміт QR-кодів.  

### 3. `authorization.html` — Авторизація
- **Мета**: Забезпечує вхід у систему для зареєстрованих користувачів.  
- **Особливості**:  
  - Перевірка логіну, пароля та email через POST-запит.  
  - Повідомлення про помилку, якщо дані некоректні.  
- **Приклад коду** (HTML-форма):  
  ```html
  <form method="POST" action="{% url 'authorization' %}">
      {% csrf_token %}
      <input type="text" id="name" name="name" required>
      <input type="password" id="password" name="password" required>
      <input type="email" id="email-confirm" name="email-confirm" required>
      <button type="submit">Авторизуватися</button>
  </form>
  ```

### 4. `free.html`, `standard.html`, `pro.html`, `desktop.html` — Сторінки генерації QR-кодів
- **Мета**: Генерація QR-кодів залежно від обраного плану підписки.  
- **Особливості**:  
  - **Free**: базові функції (розмір, посилання).  
  - **Standard**: додані кольори та форми.  
  - **Pro**: логотипи, градієнти, більше розмірів.  
  - **Desktop**: повний функціонал для локального використання.  
- **Унікальна механіка**:  
  - Збереження QR-кодів у базі даних із прив’язкою до користувача та плану.  
  - Налаштування градієнтів, форм елементів і заокруглення кутів.  
- **Приклад коду** (генерація у `free`):  
  ```python
  def render_free(request: HttpResponse):
      if not request.user.is_authenticated:
          return redirect("authorization")
      subscriber, created = Subscribers.objects.get_or_create(user=request.user)
      if subscriber.plan == 'free' and subscriber.qr_code_count >= 1:
          return render(request, "free.html", {"show_limit_modal": True})
      if request.method == "POST":
          name = request.POST.get("name")
          link = request.POST.get("link_or_text")
          size = int(request.POST.get("size", 300))
          qr_color = request.POST.get("qr_color", "#000000")
          bg_color = request.POST.get("bg_color", "#FFFFFF")
          logo_file = request.FILES.get("logo")
          use_gradient = request.POST.get("gradient") == "on"
          color1 = request.POST.get("color1", "#ff0000")
          color2 = request.POST.get("color2", "#00ff00")
          shape = request.POST.get("shape", "square")
          round_corners = shape == "rounded"
          element_shape = request.POST.get("element_shape", "square")
          if not name or not link:
              return render(request, "free.html", {"error": "Заповніть всі поля"})
          try:
              qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
              qr.add_data(link)
              qr.make(fit=True)
              img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert("RGBA")
              if element_shape == "circle":
                  mask = Image.new("L", img.size, 0)
                  draw = ImageDraw.Draw(mask)
                  for x in range(0, img.size[0], qr.box_size):
                      for y in range(0, img.size[1], qr.box_size):
                          box = (x, y, x + qr.box_size, y + qr.box_size)
                          draw.ellipse(box, fill=255)
                  img.putalpha(mask)
              elif element_shape == "triangle":
                  mask = Image.new("L", img.size, 0)
                  draw = ImageDraw.Draw(mask)
                  for x in range(0, img.size[0], qr.box_size):
                      for y in range(0, img.size[1], qr.box_size):
                          box = [(x, y + qr.box_size), (x + qr.box_size // 2, y), (x + qr.box_size, y + qr.box_size)]
                          draw.polygon(box, fill=255)
                  img.putalpha(mask)
              if use_gradient:
                  gradient = Image.new("RGBA", img.size)
                  draw = ImageDraw.Draw(gradient)
                  for y in range(img.size[1]):
                      r = int((1 - y / img.size[1]) * int(color1[1:3], 16) + (y / img.size[1]) * int(color2[1:3], 16))
                      g = int((1 - y / img.size[1]) * int(color1[3:5], 16) + (y / img.size[1]) * int(color2[3:5], 16))
                      b = int((1 - y / img.size[1]) * int(color1[5:7], 16) + (y / img.size[1]) * int(color2[5:7], 16))
                      draw.line([(0, y), (img.size[0], y)], fill=(r, g, b, 255))
                  qr_data = img.getdata()
                  gradient_data = gradient.getdata()
                  new_data = []
                  for i in range(len(qr_data)):
                      if qr_data[i][0] < 128:
                          new_data.append(gradient_data[i])
                      else:
                          new_data.append((255, 255, 255, 0))
                  img.putdata(new_data)
              img = img.resize((size, size), Image.Resampling.LANCZOS)
              if round_corners:
                  corner_radius = int(size * 0.1)
                  qr_mask = Image.new('L', img.size, 0)
                  draw = ImageDraw.Draw(qr_mask)
                  qr_box = img.getbbox()
                  draw.rounded_rectangle(qr_box, corner_radius, fill=255)
                  output = Image.new('RGBA', img.size, (0, 0, 0, 0))
                  output.paste(img, mask=qr_mask)
                  img = output
              if logo_file:
                  try:
                      logo = Image.open(logo_file).convert("RGBA")
                      logo_size = int(size * 0.25)
                      logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
                      pos_x = (size - logo_size) // 2
                      pos_y = (size - logo_size) // 2
                      logo_bg = Image.new('RGBA', (logo_size, logo_size), (255, 255, 255, 255))
                      img.paste(logo_bg, (pos_x, pos_y))
                      img.paste(logo, (pos_x, pos_y), logo)
                  except Exception as e:
                      print(f"Error processing logo: {e}")
              buffer = BytesIO()
              img.save(buffer, format="PNG")
              user_folder = os.path.join(settings.MEDIA_ROOT, request.user.username)
              if not os.path.exists(user_folder):
                  os.makedirs(user_folder)
              file_path = os.path.join(user_folder, f"{name}.png")
              with open(file_path, 'wb') as f:
                  f.write(buffer.getvalue())
              qr_image_url = os.path.join(settings.MEDIA_URL, request.user.username, f"{name}.png")
              if qr_code.objects.filter(name=name).exists():
                  return render(request, "free.html", {"error": "QR-код із таким ім'ям вже існує"})
              creation_time = timezone.now() + timedelta(hours=2)
              qr_code_instance = qr_code(
                  name=name,
                  link=link,
                  size=size,
                  shape=1 if round_corners else 0,
                  custom_style="gradient" if use_gradient else "default",
                  data_create=creation_time,
                  expiry_date=(creation_time + timedelta(days=30)).timestamp(),
                  image=qr_image_url,
                  plan_created="free",
                  user=request.user
              )
              qr_code_instance.save()
              subscriber.qr_code_count += 1
              subscriber.save()
              return render(request, "free.html", {"qr_image_url": qr_image_url})
          except Exception as e:
              print(f"Error generating QR code: {e}")
              return render(request, "free.html", {"error": "Помилка при генерації QR-коду"})
      return render(request, "free.html")
  ```
- **Принцип роботи підписок**:  
  - Кожен план має ліміт QR-кодів (`qr_code_limit` у моделі `Subscribers`).  
  - При генерації перевіряється поточна кількість (`qr_code_count`) та доступність функцій.  

---

### Моделі даних
Ці моделі, розташовані у файлі `home/models.py`, визначають структуру даних для користувачів, підписок і QR-кодів у базі даних SQLite3.

#### Модель `Subscribers`
- **Мета**: Зберігає інформацію про підписників, їхній план і кількість створених QR-кодів.  
- **Поля**:  
  - `user`: зв’язок один до одного з моделлю `User` (автентифікація Django).  
  - `subscriber`: ім’я підписника (рядок).  
  - `qr_code_count`: кількість створених QR-кодів (ціле число, за замовчуванням 0).  
  - `plan`: тип підписки (рядок, за замовчуванням "free").  
  - `qr_code_limit`: максимальна кількість QR-кодів для плану (ціле число, за замовчуванням 10).  
  - `balance`: баланс користувача (десяткове число, за замовчуванням 0.00).  
- **Приклад коду**:  
  ```python
  from django.db import models
  from django.contrib.auth.models import User

  class Subscribers(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      subscriber = models.CharField(max_length=255)
      qr_code_count = models.IntegerField(default=0)
      plan = models.CharField(max_length=10, default='free')
      qr_code_limit = models.IntegerField(default=10)
      balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

      def __str__(self):
          return self.subscriber
  ```

#### Модель `qr_code`
- **Мета**: Зберігає інформацію про кожен згенерований QR-код, включаючи його параметри та зв’язок із користувачем.  
- **Поля**:  
  - `user`: зв’язок із моделлю `User` (зовнішній ключ, може бути null).  
  - `name`: назва QR-коду (рядок, може бути null).  
  - `link`: URL або текст для QR-коду (рядок, за замовчуванням локальний URL).  
  - `size`: розмір QR-коду в пікселях (ціле число, за замовчуванням 300).  
  - `shape`: форма (ціле число, 0 — квадрат, 1 — заокруглений).  
  - `custom_style`: стиль оформлення (рядок, за замовчуванням "default").  
  - `data_create`: дата створення (дата і час, за замовчуванням поточний час).  
  - `expiry_date`: дата закінчення терміну дії (число з плаваючою точкою, за замовчуванням поточний час у секундах).  
  - `image`: шлях до зображення QR-коду (рядок, може бути null).  
  - `plan_created`: план, за яким створено QR-код (рядок, за замовчуванням "free").  
- **Приклад коду**:  
  ```python
  from django.db import models
  from django.contrib.auth.models import User
  from django.utils import timezone  
  import time

  class qr_code(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
      name = models.CharField(max_length=255, null=True, blank=True)
      link = models.URLField(max_length=2000, default='http://127.0.0.1:8000/')
      size = models.IntegerField(default=300)
      shape = models.IntegerField(default=0)
      custom_style = models.CharField(max_length=50, default="default")
      data_create = models.DateTimeField(default=timezone.now, null=False)
      expiry_date = models.FloatField(default=time.time)
      image = models.CharField(max_length=500, null=True, blank=True)
      plan_created = models.CharField(max_length=50, default="free")

      def __str__(self):
          return self.name or "Unnamed QR Code"
  ```

---


## Як запустити проєкт

### Локально на комп’ютері

1. **Завантажте Python**:
   - **Для Windows**:
     - Перейдіть на [офіційний сайт Python](https://www.python.org/downloads/windows/).
     - Завантажте останню версію Python.
     - Під час встановлення обов'язково поставте галочку "Add Python to PATH".
   - **Для Linux**:
     - Відкрийте термінал і виконайте команди:
       ```bash
       sudo apt update
       sudo apt install python3 python3-pip
       ```

2. **Завантажте проєкт**:
   Клонуйте репозиторій або розпакуйте архів. Відкрийте папку в IDE (наприклад, PyCharm).

3. **Встановіть залежності**:
   У терміналі виконайте:
   ```bash
   pip install -r requirements.txt
   ```
   (Перелік: `django`, `requests`, `pillow` тощо).

4. **Запустіть сервер**:
   Виконайте:
   ```bash
   python manage.py runserver
   ```
   Відкрийте `http://127.0.0.1:8000` у браузері.

### Віддалено на сервері (PythonAnywhere)
1. **Реєстрація**:  
   Створіть акаунт на [PythonAnywhere](https://www.pythonanywhere.com).  
2. **Завантажте проєкт**:  
   У розділі "Files" завантажте папку проєкту або клонуйте з GitHub.  
3. **Налаштуйте віртуальне оточення**:  
   У Bash-консолі:  
   ```bash
   mkvirtualenv myenv --python=/usr/bin/python3
   pip install -r requirements.txt
   ```  
4. **Налаштуйте веб-додаток**:  
   У розділі "Web" додайте новий додаток, виберіть "Manual configuration", вкажіть шлях до `wsgi.py` та віртуального оточення.  
5. **Запустіть**:  
   Натисніть "Reload" — проєкт доступний за URL (наприклад, `username.pythonanywhere.com`).  

---

## Висновки

### Користь першого проєкту на Django

Цей проєкт став для нас важливим кроком у вивченні веб-розробки:

- **Освоїли Django**: Навчилися використовувати Django як потужний фреймворк для створення веб-додатків. Зрозуміли, як скоротити свій код і зберегти час за допомогою вбудованих функцій, таких як ORM (Object-Relational Mapping), адміністративний інтерфейс та система маршрутизації URL.

- **Покращили навички роботи з SQLite3**: Зрозуміли принципи баз даних і навчилися працювати з різними типами зв'язків, такими як one-to-one, one-to-many, many-to-many. Це дозволило нам ефективно керувати даними та оптимізувати запити до бази даних.

- **Інтеграція фронтенду з бекендом**: Навчилися інтегрувати фронтенд (HTML, CSS, JS) із бекендом, створюючи динамічні та інтерактивні веб-додатки. Зрозуміли, як обробляти великі обсяги інформації та забезпечувати швидку і надійну роботу додатків.

- **Розвинули командну роботу**: Поглибили навички роботи в команді, навчилися ефективно спілкуватися та координувати свої дії. Використання системи контролю версій GitHub дозволило нам вести спільну роботу над проєктом, відстежувати зміни та забезпечувати якість коду.

- **Створення інтуїтивного дизайну UX/UI**: Навчилися створювати інтуїтивний та користувацький дизайн, який покращує взаємодію користувачів з додатком. Зрозуміли важливість зручності та простоти використання, а також навчилися застосовувати принципи UX/UI для покращення користувацького досвіду.

- **Розвиток аналітичних навичок**: Навчилися аналізувати вимоги користувачів та визначати оптимальні рішення для їх реалізації. Розвинули навички планування та управління проєктами, що дозволило нам ефективно керувати часом та ресурсами.

---

### Труднощі розробки
- Налаштування кастомізації QR-кодів (градієнти, логотипи) вимагало інтеграції бібліотеки **PIL**.  
- Синхронізація фронтенду й бекенду для динамічних форм була викликом.  
- Оптимізація роботи з базою даних для великих обсягів QR-кодів.  

---

### Перспективи розвитку

**Інтеграція API**: можливість генерувати QR-коди через зовнішні запити. Це дозволить автоматизувати процеси створення QR-кодів для різних завдань, таких як маркування товарів, керування запасами, ідентифікація продукції тощо.

**Розширення підписок**: нові функції (анімація, 3D-ефекти). Такі функції можуть бути корисними для маркетингових кампаній, створення інтерактивних QR-кодів, які привертають увагу клієнтів або використовуються для навчання персоналу.

### Використання в промисловості

**Сортування товарів на складі**
QR-коди можна використовувати для автоматизації процесів сортування та інвентаризації товарів на складі. Кожен товар може бути маркований унікальним QR-кодом, який містить інформацію про назву, категорію, термін придатності, місце зберігання тощо. Скануючи QR-коди за допомогою спеціальних пристроїв (наприклад, сканерів або смартфонів), працівники або роботизовані системи можуть швидко ідентифікувати товар, відстежувати його місцезнаходження та автоматично сортувати його у відповідні секції складу. Це значно підвищує ефективність роботи та зменшує кількість помилок.

**Логістика та управління ланцюгами поставок**
QR-коди можуть бути використані для відстеження товарів на всіх етапах логістичного ланцюга. Вони дозволяють автоматично фіксувати переміщення товарів, контролювати терміни доставки та оптимізувати маршрути транспортування.

**Контроль якості продукції**
У виробництві QR-коди можуть використовуватися для маркування деталей або готових виробів. Це дозволяє відстежувати історію виробництва, контролювати якість на кожному етапі та швидко виявляти дефекти.

**Автоматизація виробничих процесів**
QR-коди можуть інтегруватися з системами керування виробництвом (MES) для автоматизації таких процесів, як запуск обладнання, контроль параметрів виробництва або ведення обліку ресурсів.

**Обслуговування обладнання**
QR-коди можуть бути нанесені на обладнання для швидкого доступу до інструкцій з обслуговування, історії ремонтів або технічних специфікацій. Це полегшує роботу технічного персоналу та зменшує час простою обладнання.

**Маркетинг та зворотний зв’язок**
У промисловості QR-коди можуть використовуватися для маркетингових цілей, наприклад, для надання додаткової інформації про продукцію клієнтам або збору зворотного зв’язку.

**Енергетика та комунальні послуги**
QR-коди можуть бути використані для маркування обладнання, лічильників або інфраструктури, що дозволяє швидко отримувати інформацію про їх стан, проводити технічне обслуговування або контролювати витрати ресурсів.

**Охорона праці та безпека**
QR-коди можуть використовуватися для ідентифікації працівників, контролю доступу до небезпечних зон або надання інструкцій з техніки безпеки.

---

Цей проєкт - це не просто результат нашої роботи, це фундамент для подальшого розвитку. Він став потужним поштовхом для створення нових, ще складніших і більших проєктів, де ми зможемо застосувати набуті знання та навички, а також реалізувати свій творчий потенціал. Ми прагнемо не зупинятися на досягнутому, а постійно вдосконалюватися, відкриваючи для себе нові горизонти та досягаючи нових вершин.
