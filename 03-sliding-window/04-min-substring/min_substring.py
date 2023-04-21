def min_window(s, t):
    window = ""
    min_length = float('inf')
    w_store = {}  # store for window
    t_store = {}  # store for t

    # add characters for s and t stores, t store
    for c in t:
        if c not in t_store:  # initialize character in store
            w_store[c] = 0
            t_store[c] = 0
        t_store[c] += 1

    window_start = 0
    window_end = 0

    is_substring = check_valid_substring_function(t_store)


    while not is_substring(w_store):  # increase window
        # TODO write this function
        pass


    return window

def check_valid_substring_function(store):
    def check_valid_substring(w_store):
        for c in store:
            if w_store[c] >= store[c]:
                return False

        return True

    return check_valid_substring

def get_add_next(s):
    def add(i, store):
        if s[i] in store:
            store[s[i]] += 1
        i += 1
        return i, store

    return add

def get_remove_first(s):
    def subtract(i, store):
        if s[i] in store:
            store[s[i]] -= 1
        i += 1
        return i, store

    return subtract