import json
import asyncio
import telegram
import os
import datetime


from weather_logic import get_weather
from coin_logic import get_coin_prices


async def weather_noti(bot) -> None:
    msg = get_weather(os.environ.get("WEATHER_ENCODING"))
    chat_id = os.environ.get("CHAT_ID")
    bot.send_message(chat_id, text=msg)


async def coin_noti(bot) -> None:
    msg = get_coin_prices()
    chat_id = os.environ.get("CHAT_ID")
    bot.send_message(chat_id, text=msg)


def noti(event, context):

    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    bot = telegram.Bot(BOT_TOKEN)

    if int(datetime.datetime.now().hour) == 22:
        asyncio.run(weather_noti(bot))
    asyncio.run(coin_noti(bot))
