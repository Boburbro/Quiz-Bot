from loader import bot

from aiogram.exceptions import TelegramBadRequest

from data.models.channel_model import Channel

from data.consts import startus


async def check_subcription(channel:Channel, user_id:int)->bool:
    try:
        member = await bot.get_chat_member(chat_id=channel.id,user_id=user_id)
        return member.status in startus
    except TelegramBadRequest:
        return True