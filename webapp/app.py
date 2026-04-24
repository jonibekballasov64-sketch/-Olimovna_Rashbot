from flask import Flask, render_template
from threading import Thread
import asyncio

# 🔥 Flask
app = Flask(__name__)


# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return render_template("index.html")   # test yaratish


@app.route("/create")
def create():
    return render_template("index.html")


@app.route("/solve")
def solve():
    return render_template("solve.html")   # o‘quvchi ishlaydi


# =========================
# 🔥 BOTNI ISHGA TUSHIRISH
# =========================

def run_bot():
    import main
    from aiogram import executor

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    executor.start_polling(main.dp, skip_updates=True)


# Flask start bo‘lganda bot ham ishga tushadi
Thread(target=run_bot).start()


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
