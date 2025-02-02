import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from googletrans import Translator

# Ganti dengan token bot Telegram milikmu
TOKEN = "YOUR_BOT_TOKEN_HERE"
OWNER_ID = YOUR_TELEGRAM_ID_HERE  # Ganti dengan ID Telegram milikmu

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
translator = Translator()

# Logging
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply("Bot ini khusus untuk pemiliknya!")
        return
    await message.reply("Halo! Kirim teks yang ingin kamu terjemahkan.")

@dp.message_handler()
async def translate_text(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply("Kamu tidak punya izin untuk menggunakan bot ini.")
        return

    text = message.text
    try:
        translated = translator.translate(text, dest='en')  # Ubah ke bahasa yang diinginkan
        await message.reply(f"Terjemahan: {translated.text}")
    except Exception as e:
        await message.reply(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
