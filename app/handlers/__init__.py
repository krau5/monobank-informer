from typing import NoReturn

from aiogram.types import Message

from app.handlers import about, user
from app.config import dp, bot
from app.models import User


@dp.message_handler(commands='start', state='*')
async def _(msg: Message) -> NoReturn:
    if not User.instance_exists(msg.from_user.id):
        User.create_instance(user_id=msg.from_user.id)
        return

    await bot.send_message(msg.from_user.id, 'You are already added')
