import asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from os import environ
from aiohttp import web

API_ID = int(environ.get('API_ID', "14312602"))
API_HASH = environ.get('API_HASH', "0215ccb8afe30ffabec8e2c466260af9")
BOT_TOKEN = environ.get('BOT_TOKEN', "7317861894:AAGy29fi9tcklf7d-jkUrmixQmxEyZMX8Co")
OWNER_ID = 8199321200

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Hello World")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ram",
            bot_token=BOT_TOKEN,
            api_id=API_ID,
            api_hash=API_HASH
        )
    async def start(self):
        await super().start()    
        me = await self.get_me()
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", "8080").start()
        print(f"{me.first_name} with for Pyrogram (Layer) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped.")

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

@Bot.on_message(filters.text & filters.private & ~filters.me)
async def echo(client, message):
    if message.from_user.id == int(OWNER_ID):
        text = message.text
        try:
            await client.send_message("-1001692649079", text)
            # await client.send_message("-1002532543989", text)
            # await client.send_message("-1002691753029", text)
        except FloodWait as e:
            print(f"FloodWait: Sleeping for {e.value} seconds")
            await asyncio.sleep(e.value)
            # Retry after sleeping
            try:
                await client.send_message("-1001692649079", text)
                # await client.send_message("-1002532543989", text)
                # await client.send_message("-1002691753029", text)
            except Exception as ex:
                print(f"Failed to send message after FloodWait: {ex}")
        except Exception as ex:
            print(f"An error occurred: {ex}")
    else:
        pass

Bot().run()
