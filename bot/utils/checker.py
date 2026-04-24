def check_answers(user_answers, test_data):
    correct = 0
    wrong = []

    # 1–32
    for i in range(32):
        if user_answers[i] == test_data["q1_32"][i]:
            correct += 1
        else:
            wrong.append(i+1)

    # 33–35
    for i in range(3):
        if user_answers[32+i] == test_data["q33_35"][i]:
            correct += 1
        else:
            wrong.append(33+i)

    # 36–39 (sinonim)
    for i in range(4):
        if user_answers[35+i].lower() in test_data["q36_39"]:
            correct += 1
        else:
            wrong.append(36+i)

    # 40–44 (A/B)
    for i in range(5):
        a_user, b_user = user_answers[39+i].split("|")

        a_correct = test_data["q40_44"]["a"]
        b_correct = test_data["q40_44"]["b"]

        if a_user in a_correct:
            correct += 0.5
        else:
            wrong.append(f"{40+i}A")

        if b_user in b_correct:
            correct += 0.5
        else:
            wrong.append(f"{40+i}B")

    return correct, wrong
