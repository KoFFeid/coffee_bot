#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:44:01 2022

@author: dmitry
"""
from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
            types.BotCommand('start', 'Запуск'),
            types.BotCommand('help', 'Показать все команды'),
            types.BotCommand('my_id', 'Узнать свой id'),
        ])
    