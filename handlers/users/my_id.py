#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:32:12 2022

@author: dmitry
"""

from aiogram import types

from loader import dp

@dp.message_handler(commands='my_id')
async def show_user_id(message: types.Message):
    bot_user = message.from_user
    text = [
        f'Твой id: {bot_user.id} '
            ]
    
    await message.answer('\n'.join(text))
    
