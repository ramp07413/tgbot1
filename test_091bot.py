import asyncio
from pyrogram import Client, filters
from os import environ

API_ID = int(environ.get('API_ID', "14312602"))
API_HASH = environ.get('API_HASH', "0215ccb8afe30ffabec8e2c466260af9")
BOT_TOKEN = environ.get('BOT_TOKEN', "7317861894:AAGy29fi9tcklf7d-jkUrmixQmxEyZMX8Co")

Bot = Client(
    name="botoz",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

TARGET_CHAT_ID = "-1001692649079"  # yahan message bhejna hai

@Bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello! Send me a message and I will forward it to the group.")

@Bot.on_message(filters.text)
async def echo(client, message):
    if message.chat.type == "private":
        print("Received a private message:", message.text)
        try:
            await client.send_message(TARGET_CHAT_ID, message.text)
            print("Message forwarded successfully.")
        except Exception as e:
            print("Failed to send message:", e)
    else:
        print("Received group message, ignoring.")

Bot.run()
