import os
from dotenv import load_dotenv

load_dotenv()

def get_bot_password():
    return os.getenv('password')

def get_bot_login():
    return os.getenv('login')
