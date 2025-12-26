import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from routers.lesson_45 import router_45
from routers.lesson_46 import router_46
from routers.comands_router import router_com


API_TOKEN = "8024334721:AAF5YSu2nHNJJ-zIDhEkE5iQeeI5TB1FTak"
lessons = ["lesson_45",
           "lesson_46",
           "lesson_47",
           "lesson_48",
           "lesson_49",
           "lesson_50"
           ]

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
dp.include_router(router_com)
dp.include_router(router_45)
dp.include_router(router_46)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

