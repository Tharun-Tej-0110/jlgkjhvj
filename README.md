# Telegram Bot for Render

This repository contains a simple Telegram bot written in Python, ready to be deployed to Render.

## Requirements

- Python 3.8+
- `python-telegram-bot` library
- `Flask` library

## Deployment

1. Clone this repository:
    ```sh
    git clone https://github.com/your-username/telegram-bot.git
    ```
2. Add your bot token to Render's environment variables as `TELEGRAM_TOKEN`.
3. Add the webhook URL (your Render web service URL) as `WEBHOOK_URL` once the service is live.
4. Deploy the service using Render by connecting your GitHub repository and configuring as per `render.yaml`.

After deployment, set up your webhook by accessing `/set_webhook` endpoint on your Render service:
