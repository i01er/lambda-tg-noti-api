import json, os
import telegram
import asyncio
import json
from types import SimpleNamespace
# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

async def async_handler(event, context):
    token = os.environ.get('bot_token')
    chatID = os.environ.get('chat_id')
    
    # print(event)
    d_body = json.dumps(event)
    body = json.loads(d_body)
    msg = body["body"]
    temp_msg = json.loads(msg)
    
    if(event and temp_msg["pwd"] == "testing123"):
        # print(event)
        bot = telegram.Bot(token)
        await bot.send_message(text=temp_msg["text"], chat_id=chatID)
    
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': 'success'
        }
    else:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': 'fail'
        }

def lambda_handler(event, context):
    # TODO implement
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(async_handler(event, context))