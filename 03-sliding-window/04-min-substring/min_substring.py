def min_window(s, t):
    min_window = ""
    w_store = {} # store for window
    t_store = {} # store for t

    # add characters for s and t stores, t store
    for c in t:
        if c not in t_store:
            w_store[c] = 0
            t_store[c] = 0
        t_store[c] += 1


    return min_window

