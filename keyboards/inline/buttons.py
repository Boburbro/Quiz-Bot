from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from data.config import CHANNEL_ID
from data.models.channel_model import Channel

# _subscription_button = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Kanalga a'zo bo'lish", url=f"https://t.me/{CHANNEL_ID.lstrip('@')}")
#         ],
#     ]
# )

def subscription_button(channels: list[Channel]):
    buttons = [
        InlineKeyboardButton(text=f"{channel.title}", url=channel.link)
        for channel in channels
    ]
    return InlineKeyboardMarkup(inline_keyboard=[buttons])


