def check_all(user_answers, correct_answers):
    responses = []
    wrong = []

    # 1–35
    for i in range(1, 36):
        u = (user_answers.get(f"q{i}") or "").upper()
        c = (correct_answers.get(f"q{i}") or "").upper()

        if u == c:
            responses.append(1)
        else:
            responses.append(0)
            wrong.append(i)

    # 36–39 (sinonim)
    for i in range(36, 40):
        u = (user_answers.get(f"q{i}") or "").strip().lower()
        c_list = [x.lower() for x in correct_answers.get(f"q{i}", [])]

        if u in c_list:
            responses.append(1)
        else:
            responses.append(0)
            wrong.append(i)

    # 40–44 (A/B)
    for i in range(40, 45):
        u = user_answers.get(f"q{i}", {})

        ua = (u.get("a") or "").strip().lower()
        ub = (u.get("b") or "").strip().lower()

        ca = [x.lower() for x in correct_answers.get(f"q{i}", {}).get("a", [])]
        cb = [x.lower() for x in correct_answers.get(f"q{i}", {}).get("b", [])]

        if ua in ca and ub in cb:
            responses.append(1)
        else:
            responses.append(0)
            wrong.append(i)

    correct = sum(responses)
    wrong_count = 44 - correct

    return responses, correct, wrong_count, wrong
