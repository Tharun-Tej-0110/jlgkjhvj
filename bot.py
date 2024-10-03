import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Define the start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot!')

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook() -> str:
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/set_webhook", methods=["GET"])
def set_webhook() -> str:
    url = os.getenv("WEBHOOK_URL")
    if not url:
        return "Error: No WEBHOOK_URL provided", 400

    webhook_url = f"{url}/{TOKEN}"
    bot.set_webhook(webhook_url)
    return f"Webhook set to {webhook_url}"

if __name__ == '__main__':
    # Set up Flask server
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
