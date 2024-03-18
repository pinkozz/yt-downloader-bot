from aiogram import types, Bot, executor, Dispatcher
from pytube import YouTube

bot = Bot(token='')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome_message(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Welcome to Youtube Downloader bot! Please send me a link to youtube video and I will download it.")

def download_video(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    youtubeObject.download(filename="video.mp4")

@dp.message_handler()
async def send_video(message: types.Message):
    try:
        download_video(message.text)
        await bot.send_video(chat_id=message.chat.id, video=open("video.mp4", "rb"), width=1280, height=720, caption="Here is your video! Thanks for using YouDownload bot!")
    except Exception as e:
        await bot.send_message(chat_id=message.chat.id, text="An error occurred.")
        print(f"{e}")
executor.start_polling(dp)
