import json
import asyncio
import telegram
import os

from weathertest import get_raw_weather, process_weather


async def sendmsg() -> None:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
    bot = telegram.Bot(BOT_TOKEN)

    raw = get_raw_weather(os.environ.get("WEATHER_ENCODING"))
    msg = process_weather(raw)

    bot.send_message(CHAT_ID, text=msg)


def noti(event, context):
    asyncio.run(sendmsg())
