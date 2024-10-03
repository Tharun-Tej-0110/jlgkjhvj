import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot!')

def main():
    # Load the bot token from the environment variable
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TOKEN:
        raise ValueError("No TELEGRAM_TOKEN provided")

    # Set up the Updater and Dispatcher
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
