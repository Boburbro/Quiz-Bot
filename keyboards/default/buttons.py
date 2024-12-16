from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


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