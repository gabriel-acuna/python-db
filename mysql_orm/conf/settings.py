import os
from pathlib import Path  # python3 only
from dotenv import load_dotenv
load_dotenv()

load_dotenv(verbose=True)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def get_db_credentials():
    return {
    'HOST': os.getenv('DB_HOST'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'DB': os.getenv('DB')

}
