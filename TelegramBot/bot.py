from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import random

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, Таня! Я MOJbot.\nНапиши /weather, чтобы узнать погоду, или /joke, чтобы услышать анекдот!"
    )

# Команда /weather
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Запрос к API погоды
        url = "https://api.open-meteo.com/v1/forecast?latitude=56.95&longitude=24.11&current_weather=true"
        response = requests.get(url)
        response.raise_for_status()

        # Извлечение данных
        data = response.json()
        temperature = data['current_weather']['temperature']
        wind_speed = data['current_weather']['windspeed']

        await update.message.reply_text(
            f"Сейчас в Риге {temperature}°C.\nСкорость ветра: {wind_speed} м/с."
        )
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f"Не удалось получить данные о погоде: {e}")

# Команда /joke
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Почему компьютер пошёл в школу? Чтобы учиться программированию!",
        "Почему программисты всегда путают Хэллоуин и Рождество? Потому что OCT 31 == DEC 25.",
        "Как программист засыпает? Закрывает теги и идёт спать!"
    ]
    random_joke = random.choice(jokes)
    await update.message.reply_text(random_joke)

# Главная функция
def main():
    TOKEN = '7056289284:AAFj6fEPTYRmox6H4oAPiFwt4TrazZCeVCU'  # Вставь свой токен сюда

    # Настраиваем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('weather', weather))
    application.add_handler(CommandHandler('joke', joke))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
