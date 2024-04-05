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

class Reference:
    def __init__(self) -> None:
        self.response = ""

reference = Reference()

def clear_past():
    reference.response = ""

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    '''This handler receives messages with `\start` command

    Args:
         message (types.Message): _description_    
    '''
    await message.reply("Hi!\n I'am a chat bot! created by Dushyant. How can I assist you?")

if __name__ == "__main__":
   executor.start_polling(dispatcher, skip_updates=True)
   # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    #asyncio.run(main())    

