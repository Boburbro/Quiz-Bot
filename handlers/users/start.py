from aiogram.filters import CommandStart
from loader import dp,bot,Dispatcher
from aiogram import types
from utils import check_subcription
from data.config import CHANNEL_ID
from keyboards.inline.buttons import subscription_button, test_buttons

@dp.message(CommandStart())
async def start_bot(message:types.Message):
    user_id = message.from_user.id
    is_subscribed = await check_subcription(bot, CHANNEL_ID,user_id)

    if not is_subscribed:
        await message.answer("Botdan foydalanish uchun avval kanalga aʼzo bo‘ling va undan so'ng /start buyrug'ini bering👇", reply_markup=subscription_button)
    else:
        await message.answer(
            "Botga xush kelibsiz! Quyidagi testlardan birini tanlang 👇",
            reply_markup=test_buttons
        )