import os
from dotenv import load_dotenv

load_dotenv()

# Bot token
TOKEN = os.getenv("BOT_TOKEN")

# Admin ID
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# Majburiy kanallar
CHANNELS = [
    "@NargizaOlimovna_Onatili",
    "@Attestatsiya_NargizaOlimovna"
]
