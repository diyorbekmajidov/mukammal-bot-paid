from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg:types.Message):
    chat_id = msg.chat.id
    photo = msg.photo[0].file_id
    await msg.answer_photo(photo)