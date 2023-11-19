from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("14930661"))
API_HASH = input("f0536a5c2ad076b0b648db5938cabe90") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
