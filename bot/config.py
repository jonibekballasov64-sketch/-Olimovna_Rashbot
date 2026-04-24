from dotenv import load_dotenv
import os

load_dotenv()

# BOT TOKEN (.env dan olinadi)
TOKEN = os.getenv("BOT_TOKEN")

# ADMIN ID
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# MAJBURIY KANALLAR
CHANNELS = [
    "@Attestatsiya_NargizaOlimovna",
    "@NargizaOlimovna_Onatili"
]
