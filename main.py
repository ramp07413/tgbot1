import asyncio
from pyrogram import Client, filters
from os import environ

API_ID = int(environ.get('API_ID', "14312602"))
API_HASH = environ.get('API_HASH', "0215ccb8afe30ffabec8e2c466260af9")
BOT_TOKEN = environ.get('BOT_TOKEN', "7317861894:AAGy29fi9tcklf7d-jkUrmixQmxEyZMX8Co")
OWNER_ID = 8199321200

Bot = Client(
    name="botoz",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@Bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello, This is echo bot.",
        disable_web_page_preview=True
    )

# @Bot.on_message(filters.group & filters.text)
# async def forward_from_group_to_pm(client, message):
#     await client.forward_messages(
#             chat_id=OWNER_ID,             
#             from_chat_id=message.chat.id,  
#             message_ids=message.id         
#         )

@Bot.on_message(filters.text & filters.private)
async def echo(client, message):
    if message.from_user.id == OWNER_ID:
        text = message.text
        await client.send_message("-1001692649079", text)
        # await client.send_message("-1002532543989", text)
        # await client.send_message("-1002691753029", text)
    else: 
        pass

Bot.run()
