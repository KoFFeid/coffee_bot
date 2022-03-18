#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:16:00 2022

@author: dmitry
"""

from utils.set_bot_commands import set_default_commands

async def on_startup(dp):
    import filters
    #import middlewares
    
    filters.setup(dp)
    
    from handlers import dp
    #middlewares.setup(dp)
    
   # from utils.notify_admins import on_startup_notify 
    #await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from loader import dp
    
    
    executor.start_polling(dp, on_startup=on_startup)
    
    
    
