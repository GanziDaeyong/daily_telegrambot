# import json


# def hello(event, context):
#     body = {
#         "message": "Go Serverless v3.0! Your function executed successfully!",
#         "input": event,
#     }

#     return {"statusCode": 200, "body": json.dumps(body)}

import asyncio
import telegram
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


async def sendmsg() -> None:
    bot = telegram.Bot(BOT_TOKEN)
    await bot.send_message(CHAT_ID, text="TESTING...")


asyncio.run(sendmsg())


# main()
