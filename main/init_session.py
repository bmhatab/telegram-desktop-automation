from telethon import TelegramClient, connection
import logging
import os
from main.config import Config


logging.basicConfig(level=logging.WARNING)


folder_session = os.path.join(os.getcwd(),"main/session/")

phone = Config.phone
api_id = Config.api_id
api_hash = Config.api_hash
print(phone)

client = TelegramClient(folder_session + phone, api_id, api_hash)
client.start()
if client.is_user_authorized():
	print('Login success')
else:
	print('Login fail')
client.disconnect()