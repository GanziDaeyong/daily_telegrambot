import json
import asyncio
import telegram
import os


async def sendmsg() -> None:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
    bot = telegram.Bot(BOT_TOKEN)
    # await bot.send_message(CHAT_ID, text="TESTING...")
    bot.send_message(CHAT_ID, text="TESTING...")


def noti(event, context):

    asyncio.run(sendmsg())

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
        # "mysecret": process.env.
    }

    return {"statusCode": 200, "body": json.dumps(body)}

