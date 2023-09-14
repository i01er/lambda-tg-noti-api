import json, os
import telegram
# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

async def lambda_handler(event, context):
    # TODO implement
    
    token = os.environ.get('bot_token')
    chatID = os.environ.get('chat_id')

    bot = telegram.Bot(token)
    
    await bot.send_message(text='Testing!', chat_id=chatID)
    
    return {
        'statusCode': 200,
        'body': json.dumps("finish")
    }