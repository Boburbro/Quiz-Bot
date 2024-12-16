from aiogram.filters import CommandStart
from loader import dp
from aiogram import types
from keyboards.default.buttons import test_buttons

@dp.message(CommandStart())
async def start_bot(message:types.Message):
    await message.answer(
        "Botga xush kelibsiz! Quyidagi testlardan birini tanlang 👇",
        reply_markup=test_buttons
    )