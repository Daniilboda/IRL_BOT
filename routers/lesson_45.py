from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .keyboards_45 import get_kb_45
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
router = Router()


TASK_45_1_TEXTS = [
    "— Как долго ... до станции?",
    "— Если вы ... через поле - 25 минут.",
    "Если вы любите гулять в лесу, то до станции вы ... (3) за 15 минут.",
    "Если вы ... быка, то вы ... до станции за 5 минут."
]

TASK_45_1_WRONG = {
    0 : ["ходить", "пойти"],       # для (1)
    1 : ["идёте", "пошли"],     # для (2)
    2 : ["доходите", "пошли"],  # для (3)
    3 : ["погоняете, придёте", "кормите, пойдёте"], # для (4)
}

TASK_45_1_CORRECT = {
    0 : "идти",
    1 : "пойдёте",
    2 : "дойдёте",
    3 : "возьмёте, дойдёте",
}
@router.message(F.text == "/lesson_45")
async def lesson_45_start(message: Message):
    await message.answer(
        "Урок 45 — выберите задание:",
        reply_markup=get_kb_45()
    )

# @router.callback_query(F.data == "task_45_1")
# async def lesson_45_task_1(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer("Задание 1 для урока 45")
#
# @router.callback_query(F.data == "task_45_2")
# async def lesson_45_task_2(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer("Задание 2 для урока 45")



current_index_45_1 = {}
current_index_45_2 = {}
current_index_45_3 = {}
current_index_45_4 = {}
current_index_45_5 = {}
current_index_45_6 = {}
current_buttons_45_1 = {}
current_buttons_45_2 = {}
current_buttons_45_3 = {}
current_buttons_45_4 = {}
current_buttons_45_5 = {}
current_buttons_45_6 = {}

async def send_45_1(message_or_callback, user_id):
    try:
        index = current_index_45_1[user_id]
        question = TASK_45_1_TEXTS[index]
        correct = TASK_45_1_CORRECT[index]
        all_possible_answers = TASK_45_1_WRONG[index] + [correct]
        random.shuffle(all_possible_answers)

        builder = InlineKeyboardBuilder()
        for i, answ in enumerate(all_possible_answers):
            builder.button(text=answ, callback_data=f"b_45_1_{index}_{i}")
        if index != 3:
            builder.adjust(3)
        else:
            builder.adjust(1)
        keyboard = builder.as_markup()
        current_buttons_45_1[user_id] = {
            f"b_45_1_{index}_{i}": ans for i, ans in enumerate(all_possible_answers, start=0)
        }
        current_index_45_1[user_id] = index

        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(question, reply_markup=keyboard)
        else:
            await message_or_callback.answer(question, reply_markup=keyboard)


    except Exception:
        if isinstance(message_or_callback, CallbackQuery):
            await lesson_45_start(message_or_callback.message)
        else:
            await lesson_45_start(message_or_callback)
        return
async def send_45_2(message_or_callback, user_id):
    pass

async def send_45_3(message_or_callback, user_id):
    pass
async def send_45_4(message_or_callback, user_id):
    pass
async def send_45_5(message_or_callback, user_id):
    pass

async def send_45_6(message_or_callback, user_id):
    pass

sends_45 = [send_45_1, send_45_2, send_45_3, send_45_4, send_45_5, send_45_6]
current_indexes_45 = [current_index_45_1, current_index_45_2, current_index_45_3, current_index_45_4, current_index_45_5, current_index_45_6]
@router.callback_query(F.data.startswith("task_45"))
async def start_45(callback: CallbackQuery):
    func_45 = sends_45[int(callback.data.split('_')[-1])]
    user_id = callback.from_user.id
    ind_45 = current_indexes_45[int(callback.data.split('_')[-1])]
    ind_45[user_id] = 0  # начинаем с первого вопроса
    await callback.answer()  # "убираем крутящийся кружок" на кнопке
    await func_45(callback, user_id)  # запускаем викторину

@router.callback_query(F.data.startswith("b_45_1"))
async def process_45_1_btn(callback: CallbackQuery):
    user_id = callback.from_user.id
    index = current_index_45_1.get(user_id, 0)
    buttons_text = current_buttons_45_1.get(user_id, {})

    if callback.data not in buttons_text:
        await callback.answer()
        return

    correct = TASK_45_1_CORRECT[index]
    answer = buttons_text[callback.data]

    if answer == correct:
        await callback.message.answer(f"✅ ВЕРНО БЛЯТЬ! Ваш ответ: {answer}")
    else:
        await callback.message.answer(f"❌ НЕ НИХУЯ! Правильный ответ: {correct}")
    await callback.answer()

    current_index_45_1[user_id] += 1
    await send_45_1(callback, user_id)