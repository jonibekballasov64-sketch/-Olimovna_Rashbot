import math

# 44 ta savol difficulty (boshlanishda 0, keyin o‘zgartirasiz)
B = [0.0] * 44

def _sigmoid(x):
    return 1 / (1 + math.exp(-x))

def estimate_theta(responses, max_iter=25):
    # responses: 44 ta [1/0]
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
    # θ ~ [-3,3] → 0..75
    t = max(-3, min(3, theta))
    return round((t + 3) / 6 * 75, 1)
