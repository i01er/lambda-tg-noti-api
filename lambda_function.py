import json, os
import telegram
import asyncio
# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

def lambda_handler(event, context):
    # TODO implement
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(async_handler(event, context))
    
async def async_handler(event, context):
    token = os.environ.get('bot_token')
    chatID = os.environ.get('chat_id')

    bot = telegram.Bot(token)

    await bot.send_message(text='Testing!', chat_id=chatID)
    
    return {
        'statusCode': 200,
        'body': 'success'
    }