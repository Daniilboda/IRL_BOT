from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .keyboards_45 import get_kb_45
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
import re
import textwrap
router = Router()

# 1 здание
TASK_45_1_TEXTS = [
    "— Как долго ... до станции?",
    "— Если вы ... через поле - 25 минут.",
    "Если вы любите гулять в лесу, то до станции вы ... за 15 минут.",
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


#2 задание
TASK_45_2_TEXTS = """
Мы приехали в театр, когда спектакль уже начался. В [____] концерта музыкант исполнял концерт Чайковского.
Через пять минут лекция закончится. В [____] лекции студенты обычно задают свои вопросы.
Диалог президентов продолжался 30 минут. Потом был перерыв. Все ждали [____] диалога.
Певица исполняла известную песню. Нам понравилось её [____].
"""
TASK_45_2_TEXTS = [sent.strip() for sent in TASK_45_2_TEXTS.split('\n') if sent]
TASK_45_2_CORRECT = ['начале', 'конце', 'продолжения', 'исполнение']
TARGET_45_2 = "Задание 2. Заполните пропуски однокоренными существительными."
TIP_45_2 = "продолжение,начало,исполнение,конец".split(',')
REMOVES_45_2 = {
    'начале': 'начало',
    'конце': 'конец',
    'продолжения': 'продолжение',
    'исполнение': 'исполнение'
}


# 3 задание
TASK_45_3_TEXTS = ''' Виктор сидит за <b>(стол)</b> и читает газету. Вдруг он объявление о своей <b>(смерть)</b>.

Виктор сразу позвонил своему <b>(друг)</b> Антону. — Антон! Ты читал объявление о <b>(моя смерть)</b>? — спросил Виктор.
 — Да, — ответил Антон. — А откуда ты говоришь?'''

TASK_45_3_TEXTS = [sent.strip() for sent in TASK_45_3_TEXTS.split('.')]
# print(TASK_45_3_TEXTS)
REPLACES_45 = ['столом', 'смерти', 'другу', 'моей смерти']
TASK_45_3_CORRECT = ''' Виктор сидит за <b>столом</b> и читает газету. Вдруг он объявление о своей <b>смерти</b>.

Виктор сразу позвонил своему <b>другу</b> Антону. — Антон! Ты читал объявление о <b>моей смерти</b>? — спросил Виктор.
 — Да, — ответил Антон. — А откуда ты говоришь?'''

#отправка клаиватуры 45 урока
@router.message(F.text == "/lesson_45")
async def lesson_45_start(message: Message):
    await message.answer(
        "Урок 45 — выберите задание:",
        reply_markup=get_kb_45()
    )


# 4 задание


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

#все функции для отправик примеров заданий
async def send_45_1(message_or_callback, user_id):
    try:
        index = current_index_45_1[user_id]
        question = TASK_45_1_TEXTS[index]
        correct = TASK_45_1_CORRECT[index]
        all_possible_answers = TASK_45_1_WRONG[index] + [correct]
        random.shuffle(all_possible_answers)

        builder = InlineKeyboardBuilder()
        for i, answer in enumerate(all_possible_answers):
            builder.button(text=answer, callback_data=f"b_45_1_{index}_{i}")
        if index != 3:
            builder.adjust(3)
        else:
            builder.adjust(1)
        keyboard = builder.as_markup()
        current_buttons_45_1[user_id] = {
            f"b_45_1_{index}_{i}": ans for i, ans in enumerate(all_possible_answers, start=0)
        }
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


SEND_TEXT_45_2 = ''
async def send_45_2(message_or_callback, user_id):
    try:
        global SEND_TEXT_45_2
        global TIP_45_2
        index = current_index_45_2.get(user_id, 0)
        print("send_45_2: user", user_id, "index", index)
        send_txt = textwrap.fill(SEND_TEXT_45_2 + TASK_45_2_TEXTS[index], width=60)
        formatted_text = f"{send_txt}\n\n<b>Выберите слово и напишите его с правильным окончанием:</b>\n" \
                         + "\n".join(f"<i>{word}</i>" for word in TIP_45_2)

        # message_or_callback может быть CallbackQuery или Message
        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(formatted_text)
        else:
            await message_or_callback.answer(formatted_text)
    except Exception:
        if isinstance(message_or_callback, CallbackQuery):
            await lesson_45_start(message_or_callback.message)
            del current_index_45_2[user_id]
            SEND_TEXT_45_2 = ''
            TIP_45_2 = "продолжение,начало,исполнение,конец".split(',')

        else:
            await lesson_45_start(message_or_callback)
            del current_index_45_2[user_id]
            SEND_TEXT_45_2 = ''
            TIP_45_2 = "продолжение,начало,исполнение,конец".split(',')

SEND_TEXT_45_3 = ''
async def send_45_3(message_or_callback, user_id):
    try:
        global SEND_TEXT_45_3
        index = current_index_45_3.get(user_id, 0)
        if index >= len(REPLACES_45):  # если вышли за пределы текста
            await message_or_callback.answer(textwrap.fill(TASK_45_3_CORRECT, width=60))
            await lesson_45_start(message_or_callback)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''
            return
        send_txt = textwrap.fill(SEND_TEXT_45_3 + TASK_45_3_TEXTS[index], width=60)
        formatted_text = f"{send_txt}\n\n<b>Раскройте скобки:</b>"

        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(formatted_text)
        else:
            await message_or_callback.answer(formatted_text)
    except Exception:
        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(textwrap.fill(TASK_45_3_CORRECT, width=60))
            await lesson_45_start(message_or_callback.message)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''
        else:
            await message_or_callback.answer(textwrap.fill(TASK_45_3_CORRECT, width=60))
            await lesson_45_start(message_or_callback)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''

async def send_45_4(message_or_callback, user_id):
    pass
async def send_45_5(message_or_callback, user_id):
    pass

async def send_45_6(message_or_callback, user_id):
    pass


#общий обработчик кнопок запускает для каждого задания свои current_indexes и функции для отправки сообщений
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

#callback для 1 задачи
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


@router.message()
async def handle_user_text(message: Message):
    user_id = message.from_user.id

    # Если пользователь проходит задание 45.2 (текстовое)
    if user_id in current_index_45_2:
        global SEND_TEXT_45_2
        reply = message.text.lower()
        index = current_index_45_2[user_id]
        correct_word = TASK_45_2_CORRECT[index]
        current_sentence = TASK_45_2_TEXTS[index].replace('[____]', reply)
        right_sentence = TASK_45_2_TEXTS[index].replace('[____]', correct_word)
        remove_word = REMOVES_45_2[correct_word]
        TIP_45_2.remove(remove_word)
        print(current_sentence)
        print(right_sentence)
        if current_sentence == right_sentence:
            await message.answer('✅ Верно!')
            SEND_TEXT_45_2+=right_sentence
        else:
            await message.answer(f'❌ Неверно! Правильный ответ: {correct_word}')
            SEND_TEXT_45_2+=right_sentence
        current_index_45_2[user_id]+=1
        await send_45_2(message, user_id)
        return


    #3 задание
    elif user_id in current_index_45_3:
        global SEND_TEXT_45_3
        reply = message.text.lower()
        # print(SEND_TEXT_45_3 +TASK_45_3_TEXTS[i])
        index = current_index_45_3[user_id]

        if index >= len(REPLACES_45):
            await message.answer(textwrap.fill(TASK_45_3_CORRECT, width=60))
            await lesson_45_start(message)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''
            return

        if reply == REPLACES_45[index]:
            await message.answer('✅ Верно!')
            TASK_45_3_TEXTS[index] = re.sub(r'\(.*?\)', REPLACES_45[index], TASK_45_3_TEXTS[index])
            SEND_TEXT_45_3+=TASK_45_3_TEXTS[index] + '. '
        else:
            await message.answer(f'❌ Неверно! Правильный ответ: {REPLACES_45[index]}')
            TASK_45_3_TEXTS[index] = re.sub(r'\(.*?\)', REPLACES_45[index], TASK_45_3_TEXTS[index])
            SEND_TEXT_45_3+=TASK_45_3_TEXTS[index] + '. '
        current_index_45_3[user_id]+=1
        await send_45_3(message, user_id)

        print(SEND_TEXT_45_3 + TASK_45_3_TEXTS[-1])

    # # Если пользователь проходит задание 45.3
    # if user_id in current_index_45_3:
    #     await handle_task_45_3(message)
    #     return

    # Если он не в режиме теста
    # await message.answer("Напишите /lesson_45 чтобы начать.")
