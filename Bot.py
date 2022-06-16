import logging
from multiprocessing import Event
from SpeedTester import CheckSpeed, GetFileName
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import InputFile

API_TOKEN = '5510683658:AAH7uDsgXKAahwX3XlWS5PreI_9hHSx9SVU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

master = 268026070
catchLowSpeed = True

@dp.message_handler(commands=["speed"])
async def send_welcome(message: types.Message):
    if(message.from_user.id == master):
        await bot.send_message(master,"Preparing speedtest for you")
        await bot.send_photo(master, CheckSpeed()[2])

@dp.message_handler(commands=["report"])
async def GetReport(message: types.Message):
   await EveningReport(dp)

@dp.message_handler(commands=["await"])
async def CatchNormalSpeed(message: types.Message):
    catchLowSpeed = False
    await dp.bot.send_message(master, "ok, waiting for normal speed")




async def SpeedChecker(dp: Dispatcher):
    speedResult = CheckSpeed()
    if(catchLowSpeed):
        if(speedResult[0] < 300):
            await dp.bot.send_message(master, "Ahtung! Your speed is low, only " + str(speedResult[0]) + " Mb/s")
    else:
        if(speedResult[0] > 300):
            await dp.bot.send_message(master, "hallelujah! Your speed is ok now - " + str(speedResult[0]) + " Mb/s")
            catchLowSpeed = True



async def EveningReport(dp: Dispatcher):
    await dp.bot.send_message(master, "Here is your day report")
    await dp.bot.send_document(master, open(GetFileName(), 'rb'))
    


async def on_startup_notify(dp : Dispatcher):
    await dp.bot.send_message(master, "im awake")

async def on_startup(dp):
    await on_startup_notify(dp)
    scheduler.add_job(SpeedChecker,"cron", minute='0', args =(dp,))
    scheduler.add_job(EveningReport, "cron", hour='23', minute='59', args =(dp,))





if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)






