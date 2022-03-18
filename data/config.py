# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')


owner = os.getenv('owner')