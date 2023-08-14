def min_window(s, t):
    min_window_str = ""
    min_win_len = float("inf")
    w_store = {}  # store for window
    t_store = {}  # store for t

    # add characters for s and t stores, t store
    for c in t:
        if c not in t_store:
            w_store[c] = 0
            t_store[c] = 0
        t_store[c] += 1

    w_start = 0
    w_end = 0

    while w_end < len(s):
        c = s[w_end]
        w_end += 1
        if c in w_store:
            w_store[c] += 1

        while all(w_store[char] >= t_store[char] for char in t_store):
            if w_end - w_start < min_win_len:
                min_window_str = s[w_start: w_end]
                min_win_len = w_end - w_start

            c = s[w_start]
            w_start += 1
            if c in w_store:
                w_store[c] -= 1

    return min_window_str
