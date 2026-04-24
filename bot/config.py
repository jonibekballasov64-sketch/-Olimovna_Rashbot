from dotenv import load_dotenv
import os

load_dotenv()

# BOT TOKEN
TOKEN = os.getenv("BOT_TOKEN")

# ADMIN ID
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

# 🔥 KANALLAR (TO‘G‘RI PARSING)
raw_channels = os.getenv("CHANNELS", "")

CHANNELS = [ch.strip() for ch in raw_channels.split(",") if ch.strip()]
