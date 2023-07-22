import logging

from aiogram import Bot, Dispatcher, executor, types
from btn import start_menu
from inline_btn import inline, inline_btn

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "6255896092:AAHZMabMSXbeRYWSAeetX_Kf91fQRmTMKok"

bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await message.answer("""
🙋‍♀️🔸 Бот готов к использованию.
🔸 Если не появились вспомогательные кнопки намжите на это /start
""")
    
@dp.message_handler(text="🎁 Купить")
async def usluga_btn(message: types.Message):
    a = await inline()
    await message.answer("🎁 Выберите нужную вам услугу:", reply_markup=a)


@dp.message_handler(text="📱 Профиль")
async def profil_btn(message: types.Message):
    b = await inline_btn()
    await message.answer("""
    📱 Ваш профиль:
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔑 Мой ID: 2039118158
👤 Логин: @The_real_KidDeveloper
🕜 Регистрация: 20/05/2023 09:55:32
➖➖➖➖➖➖➖➖➖➖➖➖➖
💳 Баланс: 0.0 р
👥Вы пригласили: 0 человек
🔗Ссылка для приглашения: https://t.me/Probiv2bot?start=20391181584""", reply_markup=b)

@dp.message_handler(text= "ℹ️ FAQ")
async def svaz_bot(message:types.Message):
    await message.answer("""Данный бот, поможет вам найти кого угодно.
Наши плюсы:
➕Удобное использование
➕Автоматическая оплата
➕Вашим заказом занимаются профессионалы
➕Прямая связь с саппортом
➕Выдача заказа в сроки

Помощь/предложить свои услуги - @kaban_service""")

@dp.message_handler(text= "📕 Поддержка")    
async def telegram_bot(message:types.Message):
    await message.answer("📕 Писать сюда ➡️ @kaban_service")

@dp.message_handler(text= "▶️ Информация")    
async def telegram_bot(message:types.Message):
    await message.answer("""Работаем быстро и качественно ✅

Помощь/предложить свои услуги - @kaban_service""")

if __name__ == "__main__":
    executor.start_polling(dp)