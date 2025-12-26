from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_kb_46():
    builder = InlineKeyboardBuilder()
    for i in range(4):
        if i == 0:
            builder.button(
                text=f"Задание {i+1}",
                callback_data=f"task_46_{i}"
            )
        else:
            builder.button(
                text=f"❌ Задание {i+1} (в разработке)",
                callback_data=f"task_46_{i}"
            )
    builder.adjust(1, 1, 1)
    return builder.as_markup()