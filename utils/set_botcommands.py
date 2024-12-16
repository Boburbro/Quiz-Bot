from loader import bot
from aiogram.types import BotCommand
import asyncio

async def set_my_commands():
    await bot.set_my_commands(
        [
            BotCommand(command="start",description="Botni qayta ishga tushirish"),
            BotCommand(command="help", description="Yordam"),
        ]
    )


# asyncio.run(set_my_commands())