#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:24:20 2022

@author: dmitry
"""

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class IsPrivate(BoundFilter):
    key = "is_private"
    
    def __init__(self, is_private=True):
        self.is_private = is_private
        
    async def check(self, message:types.Message)->bool:
        return message.chat.type == types.ChatType.PRIVATE
        