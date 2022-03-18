#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:46:06 2022

@author: dmitry
"""

from aiogram.dispatcher.filters import BoundFilter
from data import config

from aiogram import types

class IsOwner(BoundFilter):
    key = '_is_owner'
    
    def __init__(self):
        self._is_owner = int(config.owner)
        
    async def check(self, message: types.Message):
        return message.from_user.id == self._is_owner