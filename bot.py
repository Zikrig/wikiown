import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.router import Router

from aiogram.types import Message
from aiogram import F

from to_ask import get_answer_from_query
from config import TG_TOKEN

# Включаем логирование
# logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
router = Router()

# Метод для обработки вопросов
def to_ask(question: str) -> str:
    return f"Ваш вопрос: {question}. Ответ: Это пример ответа."

# Команда /start
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот магазина glowsoul! Мы продаем массажные свечи и ароматические масла.\n Хотите узнать больше об ароматических маслах? Напишите любой вопрос, и мы ответим. Например 'от чего помогает апельсин' или 'какая температура горения массажной свечи?'")

# Команда /help
@router.message(F.text == "/help")
async def send_help(message: Message):
    await message.answer("Я могу отвечать на вопросы. Просто напиши свой вопрос!")

# Команда /about
@router.message(F.text == "/about")
async def send_about(message: Message):
    await message.answer("Я бот, созданный для демонстрации работы с aiogram.")


# Обработка текстовых сообщений (вопросов)
@router.message()
async def handle_question(message: Message):
    question = message.text
    await message.answer('Думаем...')
    answer = await get_answer_from_query(question)
    await message.answer(answer)

# Регистрация роутера и запуск бота
if __name__ == "__main__":
    dp.include_router(router)
    dp.run_polling(bot)