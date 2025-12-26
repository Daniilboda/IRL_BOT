from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .keyboards_46 import get_kb_46
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .comands_router import lesson_46_start

import random
import re
import textwrap
router_46 = Router()


# Задание 1: предлоги
TASK_46_1_TEXTS = [
    "1) Студент правильно отвечает ... вопрос.",
    "2) Музыкант исполняет ... рояле концерт Паганини.",
    "3) Туристы приехали ... выставки.",
    "4) Вчера мы получили письмо ... Михаила.",
    "5) Мы гуляли ... городском саду.",
    "6) Катя опоздала ... поезд.",
    "7) Пётр читал книгу ... автобусе.",
    "8) Анна любит вспоминать ... своём детстве.",
    "9) Дайте, пожалуйста, лекарство ... кашля."
]

# Словарь неправильных вариантов (можно менять для тестирования)
TASK_46_1_WRONG = {
    0: ["от", "с"],              # 1
    1: ["в", "о"],               # 2
    2: ["в", "от"],               # 3
    3: ["в", "с"],               # 4
    4: ["от", "с"],               # 5
    5: ["в", "с"],               # 6
    6: ["на", "с"],               # 7
    7: ["в", "с"],               # 8
    8: ["на", "в"],               # 9
}

# Словарь правильных ответов
TASK_46_1_CORRECT = {
    0: "на",           # 1
    1: "на",           # 2
    2: "с",           # 3
    3: "от",           # 4
    4: "в",            # 5
    5: "на",           # 7
    6: "в",            # 9
    7: "о",            # 10
    8: "от",           # 11
}


current_index_46_1 = {}

current_buttons_46_1 = {}
async def send_46_1(message_or_callback, user_id):
    try:
        index = current_index_46_1[user_id]
        question = TASK_46_1_TEXTS[index]
        correct = TASK_46_1_CORRECT[index]
        all_possible_answers = TASK_46_1_WRONG[index] + [correct]
        random.shuffle(all_possible_answers)

        builder = InlineKeyboardBuilder()
        for i, answer in enumerate(all_possible_answers):
            builder.button(text=answer, callback_data=f"b_46_1_{index}_{i}")
        builder.adjust(3)
        keyboard = builder.as_markup()
        current_buttons_46_1[user_id] = {
            f"b_46_1_{index}_{i}": ans for i, ans in enumerate(all_possible_answers, start=0)
        }
        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(question, reply_markup=keyboard)
        else:
            await message_or_callback.answer(question, reply_markup=keyboard)
    except Exception:
        if isinstance(message_or_callback, CallbackQuery):
            await lesson_46_start(message_or_callback.message)
        else:
            await lesson_46_start(message_or_callback)
        return

sends_46 = [send_46_1]
current_indexes_46 = [current_index_46_1]
@router_46.callback_query(F.data.startswith("task_46"))
async def start_46(callback: CallbackQuery):
    # func_46 = sends_46[int(callback.data.split('_')[-1])]
    # user_id = callback.from_user.id
    # ind_46 = current_indexes_46[int(callback.data.split('_')[-1])]
    # ind_46[user_id] = 0  # начинаем с первого вопроса
    # await callback.answer()  # "убираем крутящийся кружок" на кнопке
    # await func_46(callback, user_id)  # запускаем викторину
    if int(callback.data.split('_')[-1]) == 0:
        func_46 = sends_46[int(callback.data.split('_')[-1])]
        user_id = callback.from_user.id
        ind_46 = current_indexes_46[int(callback.data.split('_')[-1])]
        ind_46[user_id] = 0  # начинаем с первого вопроса
        await callback.answer()  # "убираем крутящийся кружок" на кнопке
        await func_46(callback, user_id)  # запускаем викторину
    else:
        await callback.answer()
        await callback.message.answer(f"Над этим заданием ведется работа")
@router_46.callback_query(F.data.startswith("b_46_1"))
async def process_46_1_btn(callback: CallbackQuery):
    user_id = callback.from_user.id
    index = current_index_46_1.get(user_id, 0)
    buttons_text = current_buttons_46_1.get(user_id, {})

    if callback.data not in buttons_text:
        await callback.answer()
        return

    correct = TASK_46_1_CORRECT[index]
    answer = buttons_text[callback.data]

    if answer == correct:
        await callback.message.answer(f"✅ Верно! Ваш ответ: {answer}")
    else:
        await callback.message.answer(f"❌ Неверно! Правильный ответ: {correct}")
    await callback.answer()
    current_index_46_1[user_id] += 1
    await send_46_1(callback, user_id)

