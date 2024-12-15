from aiogram.exceptions import TelegramBadRequest

async def check_subcription(bot,channel_id,user_id):
    try:
        member = await bot.get_chat_member(chat_id=channel_id,user_id=user_id)
        return member.status in ["member", 'administrator', 'creator']
    except TelegramBadRequest:
        return False