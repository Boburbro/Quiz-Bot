from aiogram import types, F
from aiogram.types import CallbackQuery
from aiogram import Bot, Dispatcher
from loader import bot, dp
from keyboards.inline.buttons import test_buttons  # test_buttonsni import qilish
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

test_1_questions = [
    {"question": "1-savol: Python qaysi tilda yozilgan?", "options": ["C++", "Java", "C"], "correct_option_id": 0},
    {"question": "2-savol: Telegram botlari uchun eng mashhur kutubxona?", "options": ["Aiogram", "Numpy", "Tensorflow"], "correct_option_id": 0},
]

test_2_questions = [
    {"question": "1-savol: JavaScriptni qanday ishlatish mumkin?", "options": ["Front-end", "Back-end", "Only Database"], "correct_option_id": 0},
    {"question": "2-savol: ReactJS nima?", "options": ["Frontend Framework", "Backend Framework", "Library"], "correct_option_id": 2},
]

user_results = {}

# Testni boshlash
async def start_test_1(message: types.Message):
    user_id = message.from_user.id
    user_results[user_id] = {"correct": 0, "total": len(test_1_questions)}

    for question in test_1_questions:
        await bot.send_poll(
            chat_id=message.chat.id,
            question=question["question"],
            options=question['options'],
            type="quiz",
            correct_option_id=question["correct_option_id"],
        )

    await message.answer("Test tugadi! Natijalarni hisoblayapman...")
    result = user_results[user_id]["correct"]
    total = user_results[user_id]["total"]
    await message.answer(f"Sizning natijangiz: {result}/{total}")

async def start_test_2(message: types.Message):
    user_id = message.from_user.id
    user_results[user_id] = {"correct": 0, "total": len(test_2_questions)}

    for question in test_2_questions:
        await bot.send_poll(
            chat_id=message.chat.id,
            question=question["question"],
            options=question['options'],
            type="quiz",
            correct_option_id=question["correct_option_id"],
        )

    await message.answer("Test tugadi! Natijalarni hisoblayapman...")
    result = user_results[user_id]["correct"]
    total = user_results[user_id]["total"]
    await message.answer(f"Sizning natijangiz: {result}/{total}")

# Test 1 tugmasi bosilganda
@dp.message(F.text == "Test 1 📝")
async def handle_test_1(message: types.Message):
    await start_test_1(message)

# Test 2 tugmasi bosilganda
@dp.message(F.text == "Test 2 📝")
async def handle_test_2(message: types.Message):
    await start_test_2(message)
