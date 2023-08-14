def find_repeated_sequences(s, k):
    unique_substrings = set()  # set for all unique substrings
    repeat_sequences = set()  # set for repeated substrings
    for i in range(0, len(s)-k):  # iterate over k length window
        substring = s[i: k+i]  # compute substring
        if substring not in unique_substrings:  # check if substring is repeat, add to repeat set
            unique_substrings.add(substring)  # sets can't have duplicates so no need to check if it already exists
        else:  # if it's not a repeat add it to unique substrings
            repeat_sequences.add(substring)
    return repeat_sequences  # return set of repeat substrings
