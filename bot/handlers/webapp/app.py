from flask import Flask, render_template, request, jsonify
import random, string

app = Flask(__name__)
TESTS = {}  # vaqtincha xotira

def gen_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    # ESSE (45) ni 0–75 orasida to‘g‘rilaymiz
    try:
        esse = int(data.get("q45", 0))
    except:
        esse = 0
    esse = max(0, min(75, esse))
    data["q45"] = esse

    code = gen_code()
    TESTS[code] = data

    text = f"""Assalomu alaykum.

🟦 1-qadam: Botga kiring
🟦 2-qadam: Start → Obuna → Qayta Start
🟦 3-qadam: «📤 Javob yuborish»
🟦 4-qadam: Test kodini kiriting

🔑 Test kodi: {code}

📝 45-savol (esse): 0–75
👉 Bot: @Olimovna_Rashbot
"""
    return jsonify({"code": code, "text": text})

if __name__ == "__main__":
    app.run()
