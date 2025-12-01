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


current_question_for_user = {}
current_buttons_for_user = {}

buttons_text = {}
dict_current_correct = {}
@dp.message(Command('test1'))
async def exercise1(message: types.Message):
    dict_correct_answers = {
        0: "-"
    }
    dict_wrong_answers = {
        0: ["в", "о", "на"]
    }

    exercise1  = [
        "Я очень заинтересован ... современным искусством."
    ]


    for index, sentence in enumerate(exercise1, 0):
            current_correct = dict_correct_answers[index]
            dict_current_correct[sentence] = current_correct
            all_possible_answers = dict_wrong_answers[index] + [current_correct]
            random.shuffle(all_possible_answers)

            current_question_for_user[message.from_user.id] = current_correct
            builder = InlineKeyboardBuilder()
            builder.button(text=all_possible_answers[0], callback_data=f"b_{index}_1")
            builder.button(text=all_possible_answers[1], callback_data=f"b_{index}_2")
            builder.button(text=all_possible_answers[2], callback_data=f"b_{index}_3")
            builder.button(text=all_possible_answers[3], callback_data=f"b_{index}_4")
            builder.adjust(3, 1)  # расположение по строкам
            keyboard = builder.as_markup()
            await message.answer(
                        sentence,
                        reply_markup=keyboard
                )

            current_buttons_for_user[message.from_user.id] = {
                f"b_{index}_1": all_possible_answers[0],
                f"b_{index}_2": all_possible_answers[1],
                f"b_{index}_3": all_possible_answers[2],
                f"b_{index}_4": all_possible_answers[3]
            }


@dp.callback_query()
async def process_btn(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in current_question_for_user:
        await callback.answer("Сначала начни викторину")
        return

    buttons_text = current_buttons_for_user.get(user_id, {})
    if callback.data not in buttons_text:
        await callback.answer()  # Игнорируем кнопки, не относящиеся к текущей викторине
        return

    correct = current_question_for_user[user_id]
    answer = buttons_text[callback.data]

    if answer == correct:
        await callback.message.answer("✅ Правильно!")
    else:
        await callback.message.answer(f"❌ Неверно! Правильный ответ: {correct}")

    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

