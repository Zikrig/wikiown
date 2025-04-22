import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Читаем переменные из .env
TG_TOKEN = os.getenv("TG_TOKEN")
DEEPSEEK_TOKEN = os.getenv("DEEPSEEK_TOKEN")
DEEPSEEK_URL = os.getenv("DEEPSEEK_URL")