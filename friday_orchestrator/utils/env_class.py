from os import getenv as env
from dotenv import load_dotenv
load_dotenv()

class EnvVariables:
    account_sid=env('account_sid')
    auth_token=env('auth_token')
    audio_bucket=env('audio_bucket')
    image_bucket=env('image_bucket')
    bot_id=env('bot_id')
    bot_alias_id=env('bot_alias_id')
    locale_id=env('locale_id')