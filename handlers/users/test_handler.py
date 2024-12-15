from aiogram import types, F
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from loader import bot, dp
import asyncio

test_1_questions = [
    {"question": "1-savol: Python qaysi tilda yozilgan?", "options": ["C++", "Java", "C"], "correct_option_id": 0},
    {"question": "2-savol: Telegram botlari uchun eng mashhur kutubxona?", "options": ["Aiogram", "Numpy", "Tensorflow"], "correct_option_id": 0},
]

test_2_questions = [
    {"question": "1-savol: JavaScriptni qanday ishlatish mumkin?", "options": ["Front-end", "Back-end", "Only Database"], "correct_option_id": 0},
    {"question": "2-savol: ReactJS nima?", "options": ["Frontend Framework", "Backend Framework", "Library"], "correct_option_id": 2},
]

user_results = {}

# Savollarni bir-biridan kutib yuborish
async def start_test_1(message: types.Message):
    user_id = message.from_user.id
    user_results[user_id] = {"correct": 0, "total": len(test_1_questions)}

    for question in test_1_questions:
        # Har bir savolni yuborish
        question_message = await bot.send_poll(
            chat_id=message.chat.id,
            question=question["question"],
            options=question['options'],
            type="quiz",
            correct_option_id=question["correct_option_id"],
        )

        # Javobni kutish va natijalarni saqlash
        @dp.poll_answer(lambda poll_answer: poll_answer.poll_id == question_message.poll.id)
        async def process_answer(poll_answer: types.PollAnswer):
            user_results[user_id]["correct"] += (poll_answer.option_id == question["correct_option_id"])

        # Savolni yuborganidan keyin javobni kuting
        await asyncio.sleep(2)  # Bu vaqt ichida foydalanuvchidan javob kutish

    await message.answer("Test tugadi! Natijalarni hisoblayapman...")
    result = user_results[user_id]["correct"]
    total = user_results[user_id]["total"]
    await message.answer(f"Sizning natijangiz: {result}/{total}")

async def start_test_2(message: types.Message):
    user_id = message.from_user.id
    user_results[user_id] = {"correct": 0, "total": len(test_2_questions)}

    for question in test_2_questions:
        # Har bir savolni yuborish
        question_message = await bot.send_poll(
            chat_id=message.chat.id,
            question=question["question"],
            options=question['options'],
            type="quiz",
            correct_option_id=question["correct_option_id"],
        )

        # Javobni kutish va natijalarni saqlash
        @dp.poll_answer(lambda poll_answer: poll_answer.poll_id == question_message.poll.id)
        async def process_answer(poll_answer: types.PollAnswer):
            user_results[user_id]["correct"] += (poll_answer.option_id == question["correct_option_id"])

        # Savolni yuborganidan keyin javobni kuting
        await asyncio.sleep(2)  # Bu vaqt ichida foydalanuvchidan javob kutish

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
