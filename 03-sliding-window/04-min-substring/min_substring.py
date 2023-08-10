def min_window(s, t):
    min_window = ""
    w_store = {}  # store for window
    t_store = {}  # store for t

    def is_substring():
        for char in t_store:
            if w_store[char] < t_store[char]:
                return False
        return True

    # add characters for s and t stores, t store
    for c in t:
        if c not in t_store:
            w_store[c] = 0
            t_store[c] = 0
        t_store[c] += 1

    w_start = 0
    w_end = 0
    incr = True
    while w_end < len(s) or is_substring():
        if incr:
            c = s[w_end]
            w_end += 1
            if c in w_store:
                w_store[c] += 1
                if is_substring():
                    if len(min_window) == 0 or w_end - w_start< len(min_window):
                        min_window = s[w_start: w_end]
                    incr = False
        else:
            c = s[w_start]
            w_start += 1
            if c in w_store:
                w_store[c] -= 1
            if is_substring():
                if w_end - w_start < len(min_window):
                    min_window = s[w_start: w_end]
            else:
                incr = True
    return min_window



