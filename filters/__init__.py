#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:29:18 2022

@author: dmitry
"""
from aiogram import Dispatcher

from .private_chat import IsPrivate
from .owner_id import IsOwner


def setup(dp:Dispatcher):
    dp.filters_factory.bind(IsPrivate,
                            event_handlers=[dp.message_handlers])
    dp.filters_factory.bind(IsOwner,
                            event_handlers=[dp.message_handlers])