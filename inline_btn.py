from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

async def inline():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("Пробив по номеру", callback_data="btn1")
    btn2 = InlineKeyboardButton("МВД", callback_data="btn2")
    btn3 = InlineKeyboardButton("ФНС", callback_data="btn3")
    btn4 = InlineKeyboardButton("ПФР", callback_data="btn4")
    btn5 = InlineKeyboardButton("Мини-досье (автовыдача)", callback_data="btn5")
    btn6 = InlineKeyboardButton("Верефикация Готовые кошельки", callback_data="btn6")
    btn7 = InlineKeyboardButton("Мобильные операторы", callback_data="btn7")
    btn8 = InlineKeyboardButton("Флуд и рассылка", callback_data="btn8")
    btn9 = InlineKeyboardButton("Пробив КИ", callback_data="btn9")
    btn10 = InlineKeyboardButton("Сертефикат ковид", callback_data="btn10")
    btn11 = InlineKeyboardButton("✅документы", callback_data="btn11")
    inline_keyboard.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11)

    return inline_keyboard




async def inline_btn():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("💵Пополнить", callback_data="btn11")
    btn2 = InlineKeyboardButton("🛒Мои заказы", callback_data="btn12")

    inline_keyboard.add(btn1,btn2,)

    return inline_keyboard