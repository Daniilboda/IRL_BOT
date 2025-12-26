from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from .keyboards_45 import get_kb_45
from aiogram.types import Message, CallbackQuery
from .keyboards_46 import get_kb_46
import os
from aiogram.types.input_file import FSInputFile

router_com = Router()

flag_current_activate = 0

@router_com.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! 👋\n\n"
        "Здесь собраны практические задания и учебные материалы.\n"
        "Выбирай урок с помощью команд /lesson_45, /lesson_46 и так далее."
    )

@router_com.message(F.text == "/get_audio")
async def audio_s(message: Message):
    AUDIO_FOLDER = 'audio_for_irl'
    files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith(".mp3")]
    for file_name in files:
        file_path = os.path.join(AUDIO_FOLDER, file_name)
        audio = FSInputFile(file_path)
        await message.answer_audio(audio)

@router_com.message(F.text == "/get_link")
async def link_s(message: Message):
    with open(r'C:\Users\Daniil\IdeaProjects\TG_BOT_5\links.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            await message.answer(line)



@router_com.message(F.text == "/lesson_45")
async def lesson_45_start(message: Message):
    global flag_current_activate
    flag_current_activate = 45
    print(flag_current_activate)
    await message.answer(
        "Урок 45 — выберите задание:",
        reply_markup=get_kb_45()
    )
@router_com.message(F.text == "/lesson_46")
async def lesson_46_start(message: Message):
    global flag_current_activate
    flag_current_activate = 46
    print(flag_current_activate)
    await message.answer(
        "Урок 46 — выберите задание:",
        reply_markup=get_kb_46()
    )

