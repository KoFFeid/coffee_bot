#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:43:12 2022

@author: dmitry
"""
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


from loader import dp

@dp.message_handler(CommandHelp())
async def help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - начать диалог',
        '/help - получить справку'
            ]
    
    await message.answer('\n'.join(text))