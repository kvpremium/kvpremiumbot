from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💎 Premium"),
            KeyboardButton(text="⭐ Stars")
        ],
        [
            KeyboardButton(text="🎁 Gifts"),
            KeyboardButton(text="💰 Narxlar")
        ],
        [
            KeyboardButton(text="📞 Admin")
        ]
    ],
    resize_keyboard=True
)

premium_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎁 Gift Premium")],
        [KeyboardButton(text="👤 Akkaunt uchun Premium")],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)
