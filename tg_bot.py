import  aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from conf import token
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
import asyncio
import random

bot = Bot(token=token, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


# Данные викторины
exercise1 = [
    "Я очень заинтересован ... современным искусством.",
    "Мой друг увлекается ... старинных монет.",
    "Мы любим ... в театр по выходным.",
    "Она мечтает ... большом путешествии.",
    "Он хорошо играет ... гитаре.",
    "Дети смотрят ... интересный мультфильм.",
    "Я занимаюсь ... три раза в неделю.",
    "Им нравится ... классическую музыку.",
    "Ты собираешь ... марки или открытки?",
    "Она читает ... новые книги по психологии."
]

dict_correct_answers = {
    0: "-",
    1: "коллекционированием",
    2: "ходить",
    3: "о",
    4: "на",
    5: "-",
    6: "плаванием",
    7: "слушать",
    8: "-",
    9: "-"
}

dict_wrong_answers = {
    0: ["в", "о", "на"],
    1: ["собрать", "соберёт", "собирать"],
    2: ["ходим", "ходят", "хожу"],
    3: ["в", "на", "с"],
    4: ["в", "о", "с"],
    5: ["о", "на", "в"],
    6: ["в плавании", "плавать", "плаваю"],
    7: ["слушают", "слушаю", "слушатель"],
    8: ["о", "в", "на"],
    9: ["о", "в", "на"]
}

# Словари для хранения состояния пользователя
current_index_for_user = {}  # какой вопрос сейчас
current_buttons_for_user = {}  # кнопки для текущего вопроса

@dp.message(Command('test1'))
async def start_quiz(message: types.Message):
    user_id = message.from_user.id
    current_index_for_user[user_id] = 0  # начинаем с первого вопроса
    await send_question(message, user_id)


# Функция для отправки вопроса
async def send_question(message_or_callback, user_id):
    try:
        index = current_index_for_user[user_id]

        question = exercise1[index]
        correct = dict_correct_answers[index]
        all_possible_answers = dict_wrong_answers[index] + [correct]
        random.shuffle(all_possible_answers)

        builder = InlineKeyboardBuilder()
        for i, ans in enumerate(all_possible_answers):
            builder.button(text=ans, callback_data=f"b_{index}_{i}")
        builder.adjust(2, 2)
        keyboard = builder.as_markup()

        current_buttons_for_user[user_id] = {
            f"b_{index}_{i}": ans for i, ans in enumerate(all_possible_answers)
        }
        current_index_for_user[user_id] = index

        # корректная отправка вопроса
        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer(question, reply_markup=keyboard)
        else:
            await message_or_callback.answer(question, reply_markup=keyboard)

    except Exception:
        # корректная отправка сообщения в случае ошибки
        if isinstance(message_or_callback, CallbackQuery):
            await message_or_callback.message.answer("🎉 Викторина закончена!")
        else:
            await message_or_callback.answer("🎉 Викторина закончена!")



@dp.callback_query()
async def process_btn(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in current_index_for_user:
        await callback.answer("Сначала начни викторину")
        return

    index = current_index_for_user[user_id]
    buttons_text = current_buttons_for_user.get(user_id, {})
    if callback.data not in buttons_text:
        await callback.answer()  # игнорируем лишние кнопки
        return

    correct = dict_correct_answers[index]
    answer = buttons_text[callback.data]

    if answer == correct:
        await callback.message.answer(f"✅ ВЕРНО БЛЯТЬ! Ваш ответ: {answer}")
    else:
        await callback.message.answer(f"❌ НЕ НИХУЯ! Правильный ответ: {correct}")

    await callback.answer()

    # Переходим к следующему вопросу
    current_index_for_user[user_id] += 1
    await send_question(callback, user_id)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

