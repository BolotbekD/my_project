import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ.get('TOKEN') #внутри кавычек должны писать нужную переменную из env
