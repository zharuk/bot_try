from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем игровую клавиатуру без использования билдера -------

button_4: KeyboardButton = KeyboardButton(text= LEXICON_RU['yes_button'])
button_5: KeyboardButton = KeyboardButton(text= LEXICON_RU['no_button'])

yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_4], [button_5]], one_time_keyboard=True,
                                                     resize_keyboard=True)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1],
                                              [button_2],
                                              [button_3]],
                                    resize_keyboard=True)