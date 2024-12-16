from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Any, Dict
from aiogram.types import Message
from utils.check_subscription import check_subcription
from utils.psql.channels_psql import channels
from keyboards.inline.buttons import subscription_button

class SubscriptionMiddleware(BaseMiddleware):

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any:
        ignored_channels = []
        for channel in channels:
            if not (await check_subcription(channel=channel, user_id=event.from_user.id)):
                ignored_channels.append(channel)
        if len(ignored_channels) != 0:
            await event.answer(
                text="Iltimos, barcha kanallarga obuna bo'ling!",
                reply_markup=subscription_button(ignored_channels)
            )
        else:
            return await handler(event, data)      