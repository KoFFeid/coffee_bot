#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:14:24 2022

@author: dmitry
"""

from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from filters import IsOwner

from loader import dp




@dp.message_handler(CommandStart(), _is_owner)
async def bot_start(message:types.Message):
    bot_user = message.from_user
    text = [
        f'Привет {bot_user.username}, ты хозяин этого бота'
            ]
    
    await message.answer('\n'.join(text))