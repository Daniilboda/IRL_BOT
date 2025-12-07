from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_kb_45():
    builder = InlineKeyboardBuilder()
    for i in range(6):
        builder.button(
            text=f"Задание {i+1}",
            callback_data=f"task_45_{i}"
        )
    builder.adjust(3)
    return builder.as_markup()
