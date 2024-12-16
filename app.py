from loader import dp, bot
import asyncio
import logging
import middlewares
import handlers
import utils

logging.basicConfig(level=logging.INFO)

async def main():
    try:
        await utils.notify_admins.notify_admins()
        await utils.set_botcommands.set_my_commands()
        dp.message.middleware(middleware=middlewares.subscription.SubscriptionMiddleware())
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Polling error: {e}")

if __name__ == "__main__":    
    asyncio.run(main())
