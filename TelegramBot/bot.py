import config
import logging

from aiogram import Bot, Dispatcher, executor, types
#работа кнопок
from aiogram.dispatcher.filters import Text


#log level
logging.basicConfig(level=logging.INFO)

#bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#start message
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Математика")],
        [types.KeyboardButton(text="Английский язык")],
        [types.KeyboardButton(text="Русский язык")],
        [types.KeyboardButton(text="Белорусский язык")],
        [types.KeyboardButton(text="Физика")],
        [types.KeyboardButton(text="Биология")],
        [types.KeyboardButton(text="Химия")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери предмет"
    )
    await message.answer('''Привет! Я чат-бот студии «Шевели мозгами»
                                \nПоигрывать мышцами хорошо, а шевелить мозгами еще лучше.
                                \nПроверь свои знания по: 
                                ''', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Математика")
async def math(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Пройти сейчас")],
        [types.KeyboardButton(text="Отмена")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Пройди простой тест"
    )
    await message.answer("Пройди тест, чтобы узнать свой уровень!", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Английский язык")
async def english(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Пройти сейчас")],
        [types.KeyboardButton(text="Отмена")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Пройди простой тест"
    )
    await message.answer("Пройди тест, чтобы узнать свой уровень!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Русский язык")
async def russian(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Пройти сейчас")],
        [types.KeyboardButton(text="Отмена")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Пройди простой тест"
    )
    await message.answer("Пройди тест, чтобы узнать свой уровень!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Белорусский язык")
async def belorusian(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Пройти сейчас")],
        [types.KeyboardButton(text="Отмена")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Пройди простой тест"
    )
    await message.answer("Пройди тест, чтобы узнать свой уровень!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Физика")
async def phisics(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Пройти сейчас")],
        [types.KeyboardButton(text="Отмена")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Пройди простой тест"
    )
    await message.answer("Пройди тест, чтобы узнать свой уровень!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Биология")
async def biology(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Пройти сейчас")],
        [types.KeyboardButton(text="Отмена")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Пройди простой тест"
    )
    await message.answer("Пройди тест, чтобы узнать свой уровень!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Химия")
async def chemistry(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Пройти сейчас")],
        [types.KeyboardButton(text="Отмена")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Пройди простой тест"
    )

    @dp.message_handler(lambda message: message.text == "Пройти сейчас")
    async def chemistry1(message: types.Message):
        kb = [
            [types.KeyboardButton(text="1. Количество молекул в веществе.")],
            [types.KeyboardButton(text="2. Масcа молекул в веществе")],
            [types.KeyboardButton(text="3. Количество порций вещества.")]
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder="Выбери правильный ответ"
        )

        @dp.message_handler(lambda message: message.text == "3. Количество порций вещества.")
        async def chemistry2(message: types.Message):
            kb = [
                [types.KeyboardButton(text="1. Число Авогадро.")],
                [types.KeyboardButton(text="2. Молярный объем.")],
                [types.KeyboardButton(text="3. Масса в граммах атома углерода")]
            ]
            keyboard = types.ReplyKeyboardMarkup(
                keyboard=kb,
                resize_keyboard=True,
                input_field_placeholder="Выбери правильный ответ"
            )

            @dp.message_handler(lambda message: message.text == "1. Число Авогадро.")
            async def chemistry3(message: types.Message):
                kb = [
                    [types.KeyboardButton(text="1. Кислота.")],
                    [types.KeyboardButton(text="2. Соль.")],
                    [types.KeyboardButton(text="3. Основание.")]
                ]
                keyboard = types.ReplyKeyboardMarkup(
                    keyboard=kb,
                    resize_keyboard=True,
                    input_field_placeholder="Выбери правильный ответ"
                )

                @dp.message_handler(lambda message: message.text == "3. Основание.")
                async def chemistry3(message: types.Message):
                    kb = [
                        [types.KeyboardButton(text="1. Кислота.")],
                        [types.KeyboardButton(text="2. Соль.")],
                        [types.KeyboardButton(text="3. Основание.")]
                    ]
                    keyboard = types.ReplyKeyboardMarkup(
                        keyboard=kb,
                        resize_keyboard=True,
                        input_field_placeholder="Выбери правильный ответ"
                    )

                    await message.answer("Все правильно, рекомендуем вам выбрать повышенный курс.", reply_markup=keyboard)
                await message.answer("Ca(OH)2, NaOH, Fe(OH)2 это...", reply_markup=keyboard)
            await message.answer("6.022*10^23 это...", reply_markup=keyboard)
        await message.answer("Что такое моль?", reply_markup=keyboard)
    await message.answer("Пройди тест, чтобы узнать свой уровень!", reply_markup=keyboard)

#help message
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Вот, что я умею.")

@dp.message_handler(lambda message: message.text == "Отмена")
async def cancel_def(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Математика")],
        [types.KeyboardButton(text="Английский язык")],
        [types.KeyboardButton(text="Русский язык")],
        [types.KeyboardButton(text="Белорусский язык")],
        [types.KeyboardButton(text="Физика")],
        [types.KeyboardButton(text="Биология")],
        [types.KeyboardButton(text="Химия")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери предмет"
    )
    await message.answer("Выбери другой предмет.", reply_markup=keyboard)

#run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)