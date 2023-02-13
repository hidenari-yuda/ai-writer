import os
from dotenv import load_dotenv


def load_env():
    global USER_DATA_DIR
    global CHAT_GPT_ORGANIZATION
    global CHAT_GPT_SECRET_KEY
    global UBER_SUGGEST_EMAIL
    global UBER_SUGGEST_PASSWORD
    global DEEPL_API_KEY

    # .env ファイルをロードして環境変数へ反映
    load_dotenv(override=True)

    # 環境変数を参照
    # MYAPP_USER = os.getenv('APP_USER')
    # MYAPP_PASS = os.getenv('APP_PASS')


    USER_DATA_DIR = os.getenv('USER_DATA_DIR')

    CHAT_GPT_ORGANIZATION = os.getenv('CHAT_GPT_ORGANIZATION')
    CHAT_GPT_SECRET_KEY = os.getenv('CHAT_GPT_SECRET_KEY')

    UBER_SUGGEST_EMAIL = os.getenv('UBER_SUGGEST_EMAIL')
    UBER_SUGGEST_PASSWORD = os.getenv('UBER_SUGGEST_PASSWORD')

    DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')

