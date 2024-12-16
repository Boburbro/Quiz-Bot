from aiogram import types, F
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from loader import bot, dp
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

test_1_questions = [
    {"question": "1-savol: Python qaysi tilda yozilgan?", "options": ["C++", "Java", "C"], "correct_option_id": 0},
    {"question": "2-savol: Telegram botlari uchun eng mashhur kutubxona?", "options": ["Aiogram", "Numpy", "Tensorflow"], "correct_option_id": 0},
]

test_2_questions = [
    {"question": "1-savol: JavaScriptni qanday ishlatish mumkin?", "options": ["Front-end", "Back-end", "Only Database"], "correct_option_id": 0},
    {"question": "2-savol: ReactJS nima?", "options": ["Frontend Framework", "Backend Framework", "Library"], "correct_option_id": 2},
]

user_results = {}

@dp.message(F.text == "Test 1 📝")
async def handle_test_1(message: types.Message):
    user_id = message.from_user.id
    user_results[user_id] = {"correct": 0, "total": len(test_1_questions), 'poll_index':0, 'sended_poll_id':-1}
    poll = await bot.send_poll(
            chat_id=message.chat.id,
            question=test_1_questions[user_results[user_id]['poll_index']]["question"],
            options=test_1_questions[user_results[user_id]['poll_index']]['options'],
            type="quiz",
            correct_option_id=test_1_questions[user_results[user_id]['poll_index']]["correct_option_id"],
            is_anonymous=False,
        )
    user_results[user_id]['sended_poll_id']=poll.poll.id

@dp.poll_answer()
async def process_answer(poll_answer: types.PollAnswer):
    user_id = poll_answer.user.id
    if (user_results[user_id]['sended_poll_id']==poll_answer.poll_id):
        user_results[user_id]["correct"] += (poll_answer.option_ids[0] == test_1_questions[user_results[user_id]['poll_index']]["correct_option_id"])
        user_results[user_id]['poll_index']+=1
        print(user_results[user_id]['poll_index'])
        if len(test_1_questions) >= user_results[user_id]['poll_index']:
            user_results[user_id] = {"correct": 0, "total": len(test_1_questions), 'poll_index':0, 'sended_poll_id':-1}
            poll = await bot.send_poll(
                    chat_id=user_id,
                    question=test_1_questions[user_results[user_id]['poll_index']]["question"],
                    options=test_1_questions[user_results[user_id]['poll_index']]['options'],
                    type="quiz",
                    correct_option_id=test_1_questions[user_results[user_id]['poll_index']]["correct_option_id"],
                    is_anonymous=False,
                )
            user_results[user_id]['sended_poll_id']=poll.poll.id