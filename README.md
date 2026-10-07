# 🤖 MOJbot — Telegram Bot (Погода и Юмор)

Учебный Python-бот для Telegram, разработанный с использованием современной библиотеки **`python-telegram-bot`**. Бот умеет приветствовать пользователей, делать запросы к внешнему REST API для получения актуальной погоды, а также рассказывать тематические шутки.

---

## 📂 Структура проекта

* **`bot.py`** (или ваш основной файл со скриптом) — главная логика бота, инициализация приложения, обработчики команд (`/start`, `/weather`, `/joke`) и запуск поллинга.
* **Зависимости:** `python-telegram-bot`, `requests`.

---

## 🛠 Функционал и команды

Бот поддерживает следующие команды:
* **`/start`** — приветствует пользователя по имени и рассказывает о возможностях бота.
* **`/weather`** — выполняет GET-запрос к публичному API **Open-Meteo** и выводит текущую температуру и скорость ветра в Риге.
* **`/joke`** — выбирает и отправляет случайную шутку из заготовленного списка.

---

## 💻 Пример кода (Обработчик погоды)

```python
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "[https://api.open-meteo.com/v1/forecast?latitude=56.95&longitude=24.11&current_weather=true](https://api.open-meteo.com/v1/forecast?latitude=56.95&longitude=24.11&current_weather=true)"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temperature = data['current_weather']['temperature']
        wind_speed = data['current_weather']['windspeed']

        await update.message.reply_text(
            f"Сейчас в Риге {temperature}°C.\nСкорость ветра: {wind_speed} м/с."
        )
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f"Не удалось получить данные о погоде: {e}")




Системные требования и запуск
Python: версия 3.8 или выше.

Установка зависимостей:
Установите необходимые библиотеки через терминал:

Bash
pip install python-telegram-bot requests
Настройка токена:
Вставьте токен вашего бота, полученный от @BotFather, в переменную TOKEN в коде.

Запуск бота:

Bash
python bot.py
Татьяна Буркина
