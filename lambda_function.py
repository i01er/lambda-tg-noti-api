import json, os
import telegram
# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

def lambda_handler(event, context):
    # TODO implement
    # bot = telegram.Bot(os.getenv("bot_token"))
    token = os.environ.get['bot_token']
    return {
        'statusCode': 200,
        'body': json.dumps(token)
    }