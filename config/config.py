import os
from dotenv import load_dotenv

def get_env():
    # .env ファイルをロードして環境変数へ反映
    load_dotenv(override=True)

    # 環境変数を参照
    # MYAPP_USER = os.getenv('APP_USER')
    # MYAPP_PASS = os.getenv('APP_PASS')
    USER_DATA_DIR = os.getenv('USER_DATA_DIR')
