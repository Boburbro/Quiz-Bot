from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from data.config import CHANNEL_ID

subscription_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanalga a'zo bo'lish", url=f"https://t.me/{CHANNEL_ID.lstrip('@')}")
        ],
    ]
)

test_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Test 1 📝"),
            KeyboardButton(text="Test 2 📝")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)