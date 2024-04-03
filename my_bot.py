from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
import openai


load_dotenv()
API_TOKEN = os.getenv('telegram_token')
openai_TOKEN = os.getenv('openai_api_key')

#connect with openai
openai.api_key = openai_TOKEN

#print("OK")

model_name = "gpt-3.5"

#initialize bot

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)



