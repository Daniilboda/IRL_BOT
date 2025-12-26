from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .keyboards_45 import get_kb_45
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random
import re
import textwrap
from aiogram.filters import Command
from .comands_router import lesson_45_start
from routers.comands_router import flag_current_activate
router_45 = Router()

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
«В [____] встречи мы знакомимся.»
Через пять минут лекция закончится. В [____] лекции студенты обычно задают свои вопросы.
Диалог президентов продолжался 30 минут. Потом был перерыв. Все ждали [____] диалога.
Певица исполняла известную песню. Нам понравилось её [____].
"""
TASK_45_2_TEXTS = [sent.strip() for sent in TASK_45_2_TEXTS.split('\n') if sent]
print(TASK_45_2_TEXTS)
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
TASK_45_3_TEXTS = ''' Виктор сидит за <b>(стол)</b> и читает газету. Вдруг он увидел объявление о своей <b>(смерть)</b>.
Виктор сразу позвонил своему <b>(друг)</b> Антону. — Антон! Ты читал объявление о <b>(моя смерть)</b>? — спросил Виктор.
 — Да, — ответил Антон. — А откуда ты говоришь?'''

TASK_45_3_TEXTS = [sent.strip() for sent in TASK_45_3_TEXTS.split('.')]
# print(TASK_45_3_TEXTS)
REPLACES_45 = ['столом', 'смерти', 'другу', 'моей смерти']
TASK_45_3_CORRECT = ''' Виктор сидит за <b>столом</b> и читает газету. Вдруг увидел он увидел объявление о своей <b>смерти</b>.
Виктор сразу позвонил своему <b>другу</b> Антону. — Антон! Ты читал объявление о <b>моей смерти</b>? — спросил Виктор.
 — Да, — ответил Антон. — А откуда ты говоришь?'''




# 4 задание
TASK_45_4_TEXTS = [
    "Лекция обычно [____] в два часа.",
    "Студенты [____] писать тест десять минут назад.",
    "Завтра фильм [____] в восемь вечера.",
    "Раньше экзамены [____] июне.",
    "Я не советую вам [____] эту работу в субботу."
]


TASK_45_4_CORRECT = [
    "начинается",
    "начали",
    "начнётся",
    "начинались",
    "начинать"
]

TASK_45_4_WRONG = [
    ["начинают", "начался", "начинать"],
    ["начинают", "начинали", "начнет"],
    ["начинает", "начинался", "начинают"],
    ["начинал", "начанал", "начинаются"],
    ["начать", "начинаю", "начинается"]
]

#5 задание

# Тексты заданий с [____] вместо пропусков
TASK_45_5_TEXTS = [
    "Сестре 15 лет, а брату 18 лет. Сестра [____] брата на 3 года.",
    "Моя [____] сестра учится в университете.",
    "Моя мама молодая, а бабушка [____].",
    "Антон любит спорт и часто [____] в теннис.",
    "Гид интересно [____] о Москве.",
    "Брат [____] со своей сестрой.",
    "Студент [____], когда будет перерыв.",
    "Скоро экзамен. Студенты занимаются в библиотеке [____].",
    "Троллейбус подошёл [____] станции метро.",
    "Троллейбус отошёл [____] остановки.",
    "Мы приехали [____] центр города.",
    "Мы всегда проходим [____] парк.",
    "Я хочу поблагодарить [____] за помощь.",
    "Преподаватель разрешил [____] написать тест завтра.",
    "Сегодня 10 февраля. Встреча будет [____].",
    "Антон болен. Уже [____] он лежит дома.",
    "Я поеду в Петербург [____].",
    "[____] перерыва студенты гуляли на улице.",
    "Я вернусь в Москву [____].",
    "Девушка вышла из [____].",
    "Банк находится перед [____].",
    "Я не хочу идти [____].",
    "Мы любим гулять по [____].",
    "Новый проспект начинается за [____].",
    "Гид рассказал о [____]."
]

# Правильные ответы
TASK_45_5_CORRECT = {
    0 : "младше",
    1 : "старшая",
    2 : "старая",
    3 : "играет",
    4 : "рассказывал",
    5 : "разговаривал",
    6 : "спросил",
    7 : "в библиотеке",
    8 : "к",
    9 : "от",
    10 : "в",
    11 : "через",
    12 : "их",
    13 : "им",
    14 : "через неделю",
    15 : "неделю",
    16 : "на неделю",
    17 : "во время",
    18 : "через неделю",
    19 : "дома",
    20 : "домом",
    21 : "домой",
    22 : "старому городу",
    23 : "старым городом",
    24 : "старом городе"
}

# Неправильные варианты
TASK_45_5_WRONG = {
    0 : ["молодая", "старшая"],
    1 : ["старая", "молодая"],
    2 : ["молодая", "младше"],
    3 : ["занимается", "делает"],
    4 : ["разговаривал", "сказал"],
    5 : ["рассказывал", "сказал"],
    6 : ["посоветовал", "попросил"],
    7 : ["на", "через"],
    8 : ["на", "у"],
    9 : ["с", "возле"],
    10 : ["на", "от"],
    11 : ["мимо", "на"],
    12 : ["им", "они"],
    13 : ["их", "они"],
    14 : ["неделя", "на неделю"],
    15 : ["за неделю", "на неделю"],
    16 : ["неделю", "на неделю"],
    17 : ["под", "через"],
    18 : ["неделю", "за неделю"],
    19 : ["домой", "дом"],
    20 : ["домой", "дом"],
    21 : ["дома", "домом"],
    22 : ["старый город", "старом городу", "старым городом"],
    23 : ["старый город", "старом городе"],
    24 : ["старый город", "старому городу", "старым городом"]
}

#отправка клаиватуры 45 урока
# @router_45.message(F.text == "/lesson_45")
# async def lesson_45_start(message: Message):
#     await message.answer(
#         "Урок 45 — выберите задание:",
#         reply_markup=get_kb_45()
#     )


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
            current_index_45_1[user_id] = 0
            await lesson_45_start(message_or_callback.message)
        else:
            current_index_45_1[user_id] = 0
            await lesson_45_start(message_or_callback)
        return


async def send_45_2(message_or_callback, user_id):
    TIP_45_2 = "продолжение,начало,исполнение,конец".split(',')
    if user_id in current_index_45_3: #чтобы задания на печать текста работали нормально
        del current_index_45_3[user_id]
    try:
        copy_TIP_45_2 = TIP_45_2.copy()
        index = current_index_45_2.get(user_id, [0, '', copy_TIP_45_2])
        print(index)
        send_txt = TASK_45_2_TEXTS[index[0]]
        print(send_txt)
        formatted_text = f"{send_txt}\n\n<b>Выберите слово и напишите его с правильным окончанием:</b>\n" \
                         + "\n".join(f"<i>{word}</i>" for word in index[2])

        # message_or_callback может быть CallbackQuery или Message
        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(formatted_text)
        else:
            await message_or_callback.answer(formatted_text)
    except Exception as e:
        print(e)
        if isinstance(message_or_callback, CallbackQuery):
            await lesson_45_start(message_or_callback.message)
            del current_index_45_2[user_id]
            # SEND_TEXT_45_2 = ''
            # TIP_45_2 = "продолжение,начало,исполнение,конец".split(',')

        else:
            await lesson_45_start(message_or_callback)
            del current_index_45_2[user_id]
            # SEND_TEXT_45_2 = ''
            # TIP_45_2 = "продолжение,начало,исполнение,конец".split(',')

SEND_TEXT_45_3 = ''
async def send_45_3(message_or_callback, user_id):
    if user_id in current_index_45_2: #чтобы задания на печать текста работали нормально
        del current_index_45_2[user_id]
    try:
        global SEND_TEXT_45_3
        index = current_index_45_3.get(user_id, 0)
        if index >= len(REPLACES_45):  # если вышли за пределы текста
            await message_or_callback.answer(TASK_45_3_CORRECT)
            await lesson_45_start(message_or_callback)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''
            return
        send_txt = SEND_TEXT_45_3 + TASK_45_3_TEXTS[index]
        formatted_text = f"{send_txt}\n\n<b>Раскройте скобки:</b>"

        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(formatted_text)
        else:
            await message_or_callback.answer(formatted_text)
    except Exception:
        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(TASK_45_3_CORRECT)
            await lesson_45_start(message_or_callback.message)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''
        else:
            await message_or_callback.answer(TASK_45_3_CORRECT)
            await lesson_45_start(message_or_callback)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''

async def send_45_4(message_or_callback, user_id):
    try:
        index = current_index_45_4[user_id]
        question = TASK_45_4_TEXTS[index]
        correct = TASK_45_4_CORRECT[index]
        all_possible_answers = TASK_45_4_WRONG[index] + [correct]
        random.shuffle(all_possible_answers)

        builder = InlineKeyboardBuilder()
        for i, answer in enumerate(all_possible_answers):
            builder.button(text=answer, callback_data=f"b_45_4_{index}_{i}")
        builder.adjust(2, 2)
        keyboard = builder.as_markup()
        current_buttons_45_4[user_id] = {
            f"b_45_4_{index}_{i}": ans for i, ans in enumerate(all_possible_answers, start=0)
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
async def send_45_5(message_or_callback, user_id):
    try:
        index = current_index_45_5[user_id]
        question = TASK_45_5_TEXTS[index]
        correct = TASK_45_5_CORRECT[index]
        all_possible_answers = TASK_45_5_WRONG[index] + [correct]
        random.shuffle(all_possible_answers)

        builder = InlineKeyboardBuilder()
        for i, answer in enumerate(all_possible_answers):
            builder.button(text=answer, callback_data=f"b_45_5_{index}_{i}")
        builder.adjust(2)
        keyboard = builder.as_markup()
        current_buttons_45_5[user_id] = {
            f"b_45_5_{index}_{i}": ans for i, ans in enumerate(all_possible_answers, start=0)
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

async def send_45_6(message_or_callback, user_id):
    pass


#общий обработчик кнопок запускает для каждого задания свои current_indexes и функции для отправки сообщений
sends_45 = [send_45_1, send_45_2, send_45_3, send_45_4, send_45_5, send_45_6]
current_indexes_45 = [current_index_45_1, current_index_45_2, current_index_45_3, current_index_45_4, current_index_45_5, current_index_45_6]
@router_45.callback_query(F.data.startswith("task_45"))
async def start_45(callback: CallbackQuery):
    func_45 = sends_45[int(callback.data.split('_')[-1])]
    user_id = callback.from_user.id
    ind_45 = current_indexes_45[int(callback.data.split('_')[-1])]
    if int(callback.data.split('_')[-1]) == 1:
        copy_TIP_45_2 = TIP_45_2.copy()
        ind_45[user_id] = ind_45.get(user_id, [0, '', copy_TIP_45_2])
    else:
        ind_45[user_id] = ind_45.get(user_id, 0)  # начинаем с первого вопроса
    await callback.answer()  # "убираем крутящийся кружок" на кнопке
    await func_45(callback, user_id)  # запускаем викторину

#callback для 1 задачи
@router_45.callback_query(F.data.startswith("b_45_1"))
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
        await callback.message.answer(f"✅ Верно! Ваш ответ: {answer}")
    else:
        await callback.message.answer(f"❌ Неверно! Правильный ответ: {correct}")
    await callback.answer()

    current_index_45_1[user_id] += 1
    await send_45_1(callback, user_id)

@router_45.message()
async def handle_user_text(message: Message):
    user_id = message.from_user.id
    #2 задание
    if user_id in current_index_45_2:
        reply = message.text.lower()
        index = current_index_45_2[user_id]
        correct_word = TASK_45_2_CORRECT[index[0]]
        current_sentence = TASK_45_2_TEXTS[index[0]].replace('[____]', reply)
        right_sentence = TASK_45_2_TEXTS[index[0]].replace('[____]', correct_word)
        remove_word = REMOVES_45_2[correct_word]
        current_index_45_2[user_id][2].remove(remove_word)
        # print(current_sentence)
        # print(right_sentence)
        if current_sentence == right_sentence:
            await message.answer('✅ Верно!')
        else:
            await message.answer(f'❌ Неверно! Правильный ответ: {correct_word}')
        current_index_45_2[user_id][0]+=1
        await send_45_2(message, user_id)
        return


    #3 задание
    elif user_id in current_index_45_3:
        global SEND_TEXT_45_3
        reply = message.text.lower()

        index = current_index_45_3[user_id]

        if index >= len(REPLACES_45):
            await message.answer(TASK_45_3_CORRECT)
            await lesson_45_start(message)
            del current_index_45_3[user_id]
            SEND_TEXT_45_3 = ''
            return

        if reply == REPLACES_45[index]:
            await message.answer('✅ Верно!')
            TEMP_REP = re.sub(r'\(.*?\)', REPLACES_45[index], TASK_45_3_TEXTS[index])

            SEND_TEXT_45_3+=TEMP_REP + '. '
            print(SEND_TEXT_45_3)
        else:
            await message.answer(f'❌ Неверно! Правильный ответ: {REPLACES_45[index]}')
            TEMP_REP = re.sub(r'\(.*?\)', REPLACES_45[index], TASK_45_3_TEXTS[index])
            SEND_TEXT_45_3+=TEMP_REP + '. '
            print(SEND_TEXT_45_3)
        current_index_45_3[user_id]+=1
        await send_45_3(message, user_id)

        #print(SEND_TEXT_45_3 + TASK_45_3_TEXTS[-1])


#callback для 4 задачи
@router_45.callback_query(F.data.startswith("b_45_4"))
async def process_45_4_btn(callback: CallbackQuery):
    user_id = callback.from_user.id
    index = current_index_45_4.get(user_id, 0)
    buttons_text = current_buttons_45_4.get(user_id, {})

    if callback.data not in buttons_text:
        await callback.answer()
        return

    correct = TASK_45_4_CORRECT[index]
    answer = buttons_text[callback.data]

    if answer == correct:
        await callback.message.answer(f"✅ Верно! Ваш ответ: {answer}")
    else:
        await callback.message.answer(f"❌ Неверно! Правильный ответ: {correct}")
    await callback.answer()

    current_index_45_4[user_id] += 1
    await send_45_4(callback, user_id)


#callback для 5 задачи
@router_45.callback_query(F.data.startswith("b_45_5"))
async def process_45_5_btn(callback: CallbackQuery):
    user_id = callback.from_user.id
    index = current_index_45_5.get(user_id, 0)
    buttons_text = current_buttons_45_5.get(user_id, {})

    if callback.data not in buttons_text:
        await callback.answer()
        return

    correct = TASK_45_5_CORRECT[index]
    answer = buttons_text[callback.data]

    if answer == correct:
        await callback.message.answer(f"✅ Верно! Ваш ответ: {answer}")
    else:
        await callback.message.answer(f"❌ Неверно! Правильный ответ: {correct}")
    await callback.answer()

    current_index_45_5[user_id] += 1
    await send_45_5(callback, user_id)
