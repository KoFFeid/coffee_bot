#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:03:38 2022

@author: dmitry
"""
from aiogram import types
from aiogram.dispatcher.filters import CommandStart


from filters import IsPrivate

from loader import dp


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message:types.Message):
    bot_user = message.from_user
    text = [
        f'Привет {bot_user.username}, это частная переписка'
            ]
    
    await message.answer('\n'.join(text))
    