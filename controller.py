def controller(x, y):
    global state
    if 230.1 <= y <= 447.2:
        if 422.5 <= x <= 682.5:
            state = 1
        elif 728 <= x <= 988:
            state = 2
        elif 1037.4 <= x <= 1241.5:
            state = 3
        else:
            state = 0
    elif 490.1 <= y <= 703.3:
        if 124.8 <= x <= 380.9:
            state = 4
        elif 422.5 <= x <= 682.5:
            state = 5
        elif 728 <= x <= 988:
            state = 6
        elif 1037.4 <= x <= 1241.5:
            state = 7
        else:
            state = 0
    elif 11 <= y <= 213 and 22 <= x <=235:
        state = 8
    else:
        state = 0
    return state

