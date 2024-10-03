# Telegram Bot for Render

This repository contains a simple Telegram bot written in Python, ready to be deployed to Render.

## Requirements

- Python 3.8+
- `python-telegram-bot` library

## Deployment

1. Clone this repository:
    ```sh
    git clone https://github.com/your-username/telegram-bot.git
    ```
2. Add your bot token to Render's environment variables as `TELEGRAM_TOKEN`.
3. Deploy the service using Render by connecting your GitHub repository and configuring as per `render.yaml`.

## Usage

- Start the bot and use `/start` command to interact with it.
