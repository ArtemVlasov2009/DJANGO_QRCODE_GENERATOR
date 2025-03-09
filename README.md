Ось оновлена версія вашого README.md, яка відповідає зазначеним вимогам. Я реорганізував вміст, додав деталі та структурував його відповідно до вашого запиту.

---

# Генератор QR-кодів

## Мета створення проєкту та його користь для користувача

**Генератор QR-кодів** — це інноваційний веб-додаток, створений для спрощення процесу генерації QR-кодів із широкими можливостями кастомізації. Наша мета — надати користувачам простий, інтуїтивний і водночас потужний інструмент для створення унікальних QR-кодів, які можна адаптувати під різні потреби: від простих посилань до складних дизайнів із логотипами та градієнтами.  

Проєкт корисний для:  
- **Індивідуальних користувачів**: швидко створювати QR-коди для особистих посилань чи тексту.  
- **Бізнесу**: генерувати брендовані QR-коди з логотипами та унікальним дизайном для маркетингу.  
- **Розробників**: досліджувати приклад реалізації веб-додатку на Django з інтеграцією бази даних і кастомізацією.  

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

Наша команда складається з трьох талановитих учасників, кожен із яких вніс унікальний внесок у проєкт:  

- **Артем Власов (Team Lead)**  
  - Роль: Керівник команди, фронтенд-розробник, дизайнер інтерфейсу.  
  - GitHub: [ArtemVlasov2009](https://github.com/ArtemVlasov2009)  
  - Відповідальність: архітектура проєкту, дизайн, основний функціонал.  

- **Ткач Богдан**  
  - Роль: Бекенд-розробник, спеціаліст із баз даних.  
  - GitHub: [Bogdantkach12](https://github.com/Bogdantkach12)  
  - Відповідальність: логіка генерації QR-кодів, робота з базою даних SQLite3.  

- **Іван Єжов**  
  - Роль: Фронтенд-розробник, дизайнер інтерфейсу.  
  - GitHub: [EzhovIvan](https://github.com/EzhovIvan)  
  - Відповідальність: стильний дизайн сторінок, інтерактивні елементи.  

---

## Посилання на Figma-дизайн та FigJam

- **Figma-дизайн**:  
  [Figma - QR Code Generator Project](https://www.figma.com/design/DdHVri8QFYcHu0aAtPD0YH/QR-Code-Generator-Project?node-id=223-92&t=ud8Q13eHWrrlpWDk-0)  
  Прототип дизайну інтерфейсу, який відображає структуру та стиль сторінок.  

- **FigJam**:  
  [FigJam](https://raw.githubusercontent.com/ArtemVlasov2009/DJANGO_QRCODE_GENERATOR/main/img_figjam/FigJam.png)  
  Схема планування проєкту, яка допомогла нам організувати задачі та ідеї.  

---

## Структура проєкту

Проєкт побудований на фреймворку **Django** і складається з кількох ключових компонентів:  
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

Ось оновлений фрагмент вашого README.md із заміненим кодом у секції для `free.html`. Я вставив ваш Python-код замість попереднього HTML-прикладу:

---

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
      # Перевірка, чи користувач авторизований
      if not request.user.is_authenticated:
          return redirect("authorization")  # Перенаправлення на сторінку авторизації, якщо не авторизований

      # Отримання або створення профілю підписника для поточного користувача
      subscriber, created = Subscribers.objects.get_or_create(user=request.user)

      # Перевірка ліміту QR-кодів для безкоштовного плану
      if subscriber.plan == 'free' and subscriber.qr_code_count >= 1:
          return render(request, "free.html", {"show_limit_modal": True})  # Відображення модального вікна з повідомленням про ліміт

      # Обробка POST-запиту (створення QR-коду)
      if request.method == "POST":
          # Отримання даних з форми
          name = request.POST.get("name")  # Ім'я QR-коду
          link = request.POST.get("link_or_text")  # Посилання або текст для QR-коду
          size = int(request.POST.get("size", 300))  # Розмір QR-коду (за замовчуванням 300)
          qr_color = request.POST.get("qr_color", "#000000")  # Колір QR-коду (за замовчуванням чорний)
          bg_color = request.POST.get("bg_color", "#FFFFFF")  # Колір фону (за замовчуванням білий)
          logo_file = request.FILES.get("logo")  # Файл логотипу (опціонально)
          use_gradient = request.POST.get("gradient") == "on"  # Використовувати градієнт (так/ні)
          color1 = request.POST.get("color1", "#ff0000")  # Перший колір градієнту (за замовчуванням червоний)
          color2 = request.POST.get("color2", "#00ff00")  # Другий колір градієнту (за замовчуванням зелений)
          shape = request.POST.get("shape", "square")  # Форма QR-коду (за замовчуванням квадрат)
          round_corners = shape == "rounded"  # Чи заокруглені кути (так/ні)
          element_shape = request.POST.get("element_shape", "square")  # Форма елементів

          # Перевірка на заповненість обов'язкових полів
          if not name or not link:
              return render(request, "free.html", {"error": "Заповніть всі поля"})  # Повідомлення про помилку

          try:
              # Генерація QR-коду
              qr = qrcode.QRCode(
                  version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10,
                  border=4,
              )
              qr.add_data(link)  # Додавання даних (посилання/текст) до QR-коду
              qr.make(fit=True)  # Автоматичне налаштування розміру
              img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert("RGBA")  # Створення зображення QR-коду

              # Зміна форми елементів QR-кода (кола, трикутники)
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

              # Застосування градієнту
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

              img = img.resize((size, size), Image.Resampling.LANCZOS)  # Зміна розміру зображення

              # Заокруглення кутів
              if round_corners:
                  corner_radius = int(size * 0.1)
                  qr_mask = Image.new('L', img.size, 0)
                  draw = ImageDraw.Draw(qr_mask)
                  qr_box = img.getbbox()
                  draw.rounded_rectangle(qr_box, corner_radius, fill=255)
                  output = Image.new('RGBA', img.size, (0, 0, 0, 0))
                  output.paste(img, mask=qr_mask)
                  img = output

              # Додавання логотипу
              if logo_file:
                  try:
                      logo = Image.open(logo_file).convert("RGBA")  # Відкриття та конвертація логотипу
                      logo_size = int(size * 0.25)  # Розмір логотипу (25% від розміру QR-коду)
                      logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)  # Зміна розміру логотипу
                      pos_x = (size - logo_size) // 2  # Позиція логотипу по X
                      pos_y = (size - logo_size) // 2  # Позиція логотипу по Y
                      logo_bg = Image.new('RGBA', (logo_size, logo_size), (255, 255, 255, 255))
                      img.paste(logo_bg, (pos_x, pos_y))
                      img.paste(logo, (pos_x, pos_y), logo)  # Вставка логотипу в центр QR-коду
                  except Exception as e:
                      print(f"Error processing logo: {e}")  # Виведення помилки

              # Збереження QR-коду
              buffer = BytesIO()
              img.save(buffer, format="PNG")  # Збереження зображення у буфер
              user_folder = os.path.join(settings.MEDIA_ROOT, request.user.username)  # Шлях до папки користувача
              if not os.path.exists(user_folder):
                  os.makedirs(user_folder)  # Створення папки користувача, якщо її не існує
              file_path = os.path.join(user_folder, f"{name}.png")  # Повний шлях до файлу
              with open(file_path, 'wb') as f:
                  f.write(buffer.getvalue())  # Запис зображення з буфера у файл
              qr_image_url = os.path.join(settings.MEDIA_URL, request.user.username, f"{name}.png")  # URL зображення

              # Перевірка на унікальність імені QR-коду
              if qr_code.objects.filter(name=name).exists():
                  return render(request, "free.html", {"error": "QR-код із таким ім'ям вже існує"})  # Повідомлення про помилку

              creation_time = timezone.now() + timedelta(hours=2)
              # Збереження інформації про QR-код в базі даних
              qr_code_instance = qr_code(
                  name=name,
                  link=link,
                  size=size,
                  shape=1 if round_corners else 0,
                  custom_style="gradient" if use_gradient else "default",
                  data_create=creation_time,
                  expiry_date=(creation_time + timedelta(days=30)).timestamp(),
                  image=qr_image_url,
                  plan_created="free",  # Вказуємо, що QR-код створено за безкоштовним планом
                  user=request.user  # Вказуємо користувача, який створив QR-код
              )
              qr_code_instance.save()  # Збереження об'єкта в базі даних

              # Збільшення лічильника QR-кодів у профілі підписника
              subscriber.qr_code_count += 1
              subscriber.save()  # Збереження змін у профілі підписника

              # Відображення QR-коду на сторінці
              return render(request, "free.html", {"qr_image_url": qr_image_url})

          except Exception as e:
              print(f"Error generating QR code: {e}")  # Виведення помилки
              return render(request, "free.html", {"error": "Помилка при генерації QR-коду"})  # Повідомлення про помилку

      # Відображення сторінки free.html (при GET-запиті або після обробки POST-запиту)
      return render(request, "free.html")
  ```

Цей код демонструє повний процес генерації QR-коду для сторінки `free.html`, включаючи перевірку авторизації, обробку форм, кастомізацію (градієнти, форми елементів, заокруглення кутів, логотипи) та збереження результату. Якщо вам потрібні додаткові пояснення чи зміни — дайте знати!
- **Принцип роботи підписок**:  
  - Кожен план має ліміт QR-кодів (`qr_code_limit` у моделі `Subscribers`).  
  - При генерації перевіряється поточна кількість (`qr_code_count`) та доступність функцій.  

---

## Як запустити проєкт

### Локально на комп’ютері
1. **Завантажте проєкт**:  
   Клонуйте репозиторій або розпакуйте архів. Відкрийте папку в IDE (наприклад, PyCharm).  
2. **Встановіть залежності**:  
   У терміналі виконайте:  
   ```bash
   pip install -r requirements.txt
   ```
   (Перелік: `django`, `requests`, `pillow` тощо).  
3. **Запустіть сервер**:  
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
- Освоїли **Django** як потужний фреймворк для створення веб-додатків.  
- Покращили навички роботи з **SQLite3** і зрозуміли принципи баз даних.  
- Навчилися інтегрувати фронтенд (HTML, CSS, JS) із бекендом.  
- Розвинули вміння працювати в команді через GitHub.  

### Труднощі розробки
- Налаштування кастомізації QR-кодів (градієнти, логотипи) вимагало інтеграції бібліотеки **PIL**.  
- Синхронізація фронтенду й бекенду для динамічних форм була викликом.  
- Оптимізація роботи з базою даних для великих обсягів QR-кодів.  

### Перспективи розвитку
- **Інтеграція API**: можливість генерувати QR-коди через зовнішні запити.  
- **Розширення підписок**: нові функції (анімація, 3D-ефекти).  

Цей проєкт — лише початок, і ми бачимо великий потенціал для його вдосконалення!
