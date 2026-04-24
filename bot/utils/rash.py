import math

# 🔥 44 ta savol difficulty (keyin o'zgartirasiz)
B = [0.0] * 44


# ======================
# RASCH HISOB
# ======================
def _sigmoid(x):
    return 1 / (1 + math.exp(-x))


def estimate_theta(responses, max_iter=25):
    theta = 0.0

    for _ in range(max_iter):
        g, h = 0.0, 0.0

        for i in range(44):
            p = _sigmoid(theta - B[i])
            u = responses[i]

            g += (u - p)
            h -= p * (1 - p)

        if abs(h) < 1e-6:
            break

        step = g / h
        theta -= step

        if abs(step) < 1e-3:
            break

    return theta


def theta_to_test_ball(theta):
    t = max(-3, min(3, theta))
    return round((t + 3) / 6 * 75, 1)


# ======================
# 44 SAVOLNI TEKSHIRISH
# ======================
def check_answers(user, correct):
    responses = []

    # 1–35 (A B C D / A–F)
    for i in range(1, 36):
        u = (user.get(f"q{i}") or "").upper()
        c = (correct.get(f"q{i}") or "").upper()
        responses.append(1 if u == c else 0)

    # 36–39 (sinonim)
    for i in range(36, 40):
        u = (user.get(f"q{i}") or "").strip().lower()
        c_list = [x.strip().lower() for x in correct.get(f"q{i}", [])]
        responses.append(1 if u in c_list else 0)

    # 40–44 (A / B)
    for i in range(40, 45):
        u = user.get(f"q{i}", {})

        ua = (u.get("a") or "").strip().lower()
        ub = (u.get("b") or "").strip().lower()

        ca = [x.strip().lower() for x in correct.get(f"q{i}", {}).get("a", [])]
        cb = [x.strip().lower() for x in correct.get(f"q{i}", {}).get("b", [])]

        ok = (ua in ca) and (ub in cb)
        responses.append(1 if ok else 0)

    correct_count = sum(responses)
    wrong_count = 44 - correct_count

    return responses, correct_count, wrong_count


# ======================
# YAKUNIY HISOB
# ======================
def calculate_result(user_answers, correct_answers, esse):
    # 1. Tekshiruv
    responses, correct, wrong = check_answers(user_answers, correct_answers)

    # 2. Rasch
    theta = estimate_theta(responses)
    test_ball = theta_to_test_ball(theta)  # 0–75

    # 3. 45 (esse)
    esse = int(esse)

    # 4. Yakuniy
    final = round((test_ball + esse) / 2, 1)

    # 5. Daraja
    if final >= 70:
        grade = "A+"
    elif final >= 65:
        grade = "A"
    elif final >= 60:
        grade = "B+"
    elif final >= 55:
        grade = "B"
    elif final >= 50:
        grade = "C+"
    elif final >= 46:
        grade = "C"
    else:
        grade = "Fail"

    return {
        "correct": correct,
        "wrong": wrong,
        "test_ball": test_ball,
        "esse": esse,
        "final": final,
        "grade": grade
    }
