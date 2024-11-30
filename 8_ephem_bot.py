import logging
import ephem
import settings
from flask import Flask, request, jsonify
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание Flask-приложения
app = Flask(__name__)

# Токен вашего бота
TELEGRAM_BOT_TOKEN = settings.token

# приложение для Telegram
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()


async def start(update, context):
    await update.message.reply_text("Привет! Используйте /planet <название>, чтобы узнать о планете.")


async def planet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 0:
        await update.message.reply_text("Пожалуйста, укажите название планеты, например: /planet Mars")
        return

    planet_name = context.args[0].capitalize()  # Получаем название планеты
    observer = ephem.Observer()

    # Выбор планеты
    if planet_name == "Mercury":
        planet = ephem.Mercury(observer)
    elif planet_name == "Venus":
        planet = ephem.Venus(observer)
    elif planet_name == "Earth":
        planet = ephem.Earth(observer)
    elif planet_name == "Mars":
        planet = ephem.Mars(observer)
    elif planet_name == "Jupiter":
        planet = ephem.Jupiter(observer)
    elif planet_name == "Saturn":
        planet = ephem.Saturn(observer)
    elif planet_name == "Uranus":
        planet = ephem.Uranus(observer)
    elif planet_name == "Neptune":
        planet = ephem.Neptune(observer)
    else:
        await update.message.reply_text(
            "Неизвестная планета. Пожалуйста, укажите одну из следующих: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.")
        return

    planet.compute(observer)
    constellation = ephem.constellation(planet)

    message = f"{planet_name} находится в созвездии: {constellation[1]}"
    await update.message.reply_text(message)


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("planet", planet))
application.start()


# Обработка входящих обновлений
@app.route('/mytgbot', methods=["GET", "POST"])
async def webhook():
    update = request.get_json()
    update_m = Update.de_json(update, application.bot)
    if not application.running:
        await application.initialize()
    await application.process_update(update_m)

    return 'ok', 200

