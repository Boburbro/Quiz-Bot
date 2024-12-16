from loader import bot
from data.config import ADMINS

async def notify_admins():
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi! /start")
        except:
            pass


# asyncio.run(notify_admins("Bot ishga tushdi! /start"))