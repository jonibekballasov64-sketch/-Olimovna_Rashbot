from dotenv import load_dotenv
import os

load_dotenv()

# BOT TOKEN
TOKEN = os.getenv("BOT_TOKEN")

# ADMIN ID
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

# MAJBURIY KANALLAR (.env dan olinadi)
CHANNELS = os.getenv("CHANNELS", "").split(",")
