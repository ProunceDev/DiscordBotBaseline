from constants import *
from interactions import *
from settings import SettingsManager
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

config = SettingsManager("config.json")
bot = Client(debug_scope=config.get_setting("guild_id", ""), intents=Intents.ALL, token=TOKEN)

class Utilities(Extension):
    pass