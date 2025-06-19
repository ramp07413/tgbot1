# ye import hai
import asyncio
from pyrogram import Client, filters
from os import environ

#ye jaruri config
API_ID = int(environ.get('API_ID', "14312602"))
API_HASH = environ.get('API_HASH', "0215ccb8afe30ffabec8e2c466260af9")
BOT_TOKEN = environ.get('BOT_TOKEN', "7317861894:AAGy29fi9tcklf7d-jkUrmixQmxEyZMX8Co")
OWNER_ID = 8199321200
# ye baad me
#PORT = environ.get("PORT", "8080")
#DATABASE_NAME = environ.get('DATABASE_NAME', "")
#DATABASE_URI = environ.get('DATABASE_URI', "")
#COLLECTION_NAME = environ.get('COLLECTION_NAME', "")

# ye telegram ka bot ke setup
Bot = Client(
    name="botoz",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

#ye cmd
@Bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello, This is echo bot.",
        disable_web_page_preview=True
    )
    pass

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