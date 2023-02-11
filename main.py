import asyncio

from aiogram import types, executor, Dispatcher, Bot
from key import my_key

bot = Bot(my_key)
dp = Dispatcher(bot)
TIME_SLEEP = 1.5


@dp.message_handler(commands=['start'])
async def hi_bots(message: types.Message):
    # await message.answer("test", reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="✅ ЗАЦIКАВИЛО ✅",
                                                                           callback_data="First_step"),
                                                )
    await bot.send_message(message.chat.id, message.from_user.first_name + ' ' + 'Привіт 😉❗')
    await asyncio.sleep(TIME_SLEEP)
    await bot.send_message(message.chat.id,
                           'Якщо ти віриш, що можна в інтернеті заробити гроші 💰💵 - то ти потрапив за адресою❗️')
    await asyncio.sleep(TIME_SLEEP)
    await bot.send_message(message.chat.id,
                           'Дивись моє відео - я постараюся максимально детально розповісти, що до чого👇👇👇👇👇👇👇👇👇👇',
                           reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'First_step')
async def process_callback(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="❗ ГОТОВИЙ ❗",
                                                                           callback_data="Second_step"))
    await callback.message.answer('123', reply_markup=keyboard)
    # reply полезень когда бот есть в чате он отвечает сообщения


@dp.callback_query_handler(lambda c: c.data == 'Second_step')
async def process_callback(callback: types.CallbackQuery):
    await callback.message.answer('123', reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton
                                                                                       (text="👉 РЕГИСТРАЦИЯ 👈",
                                                                                        url="https://vegasplay.run/")))
    await asyncio.sleep(TIME_SLEEP)
    await callback.message.answer('Натискай на кнопку «реєстрація» і зареєструй свій аккаунт '
                                  'Після реєстрації я видам тобі першу методику по заробітку !')
    await asyncio.sleep(5)
    await callback.message.answer('ТИ ВЖЕ ЗАРЕЄСТРУВАВСЯ❓\n'
                                  '✅ Якщо так , НАТИСКАЙ',
                                  reply_markup=types.InlineKeyboardMarkup().add(
                                      types.InlineKeyboardButton(text='✅ ПОЛУЧИТЬ МЕТОДИКУ ✅',
                                                                 callback_data="Third_Step")))


@dp.callback_query_handler(lambda c: c.data == 'Third_Step')
async def process_callback(callback: types.CallbackQuery):
    await callback.message.answer('Я вже готую для тебе схему 💸🤑')
    await asyncio.sleep(TIME_SLEEP)
    await callback.message.answer('❗️НИЖЧЕ я прикріпив статтю , в якій детально описана СХЕМА .\n'
                                  'Бажаємо успіху 🎯\n'
                                  '👇🏽Інструкція тут👇🏽\n'
                                  'https://telegra.ph/YAK-PRAVILNO-PROKRUTITI-01-29\n')
    await callback.message.answer('👆🏻Відео інструкція від реєстрації до виграшу 5 000 грн 👆🏻\n'
                                  '❗️ НАГАДАЮ ❗️\n'
                                  'Якщо схема ❌НЕ ПРАЦЮЄ ❌ і в тебе є відео доказ  , '
                                  'Ти можеш написати мені і я особисто виплачу тобі зі своєї кишені 5.000 тис. грн\n'
                                  '📍Підпишись на мою групу телеграмі, там додаткові новини '
                                  'та інстаграм щоб стежити на оновленнями\n'
                                  '📝Якщо залишилися питання - пиши  у особисті повідомлення , і ми їх вирішимо',
                                  reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(
                                      text='🌟ГРУППА🌟',
                                      url=""),
                                      types.InlineKeyboardButton(
                                      text='❗️ НАПИСАТЬ МНЕ ❗️',
                                      url=""
                                  )))


@dp.message_handler()
async def mess(message: types.Message):
    await bot.send_message(message.chat.id,
                           "❗️ЛИЧНАЯ СВЯЗЬ - ❗"'\n'
                           "🌟 ГРУППА ТЕЛЕГРАМ -  🌟")


if __name__ == '__main__':
    executor.start_polling(dp)