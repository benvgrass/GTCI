def min_window(str1, str2):
    idx_s1 = 0
    idx_s2 = 0
    min_substr = ''
    contains_substr = False
    start = 0
    end = 0

    while idx_s1 < len(str1):  # iterate through s1. when done with s1 we return substring
        if not contains_substr:  # looking for start and end of substring
            if str1[idx_s1] == str2[idx_s2]:  # if characters match, move to next character in str2
                idx_s2 += 1
                if idx_s2 >= len(str2):
                    contains_substr = True
                    start, end = idx_s1, idx_s1 + 1  # initialize backtrack loop variables
                    idx_s2 -= 1  # move str2 pointer to last char of s2
                    idx_s1 -= 1  # prevent completion of looping if substring ends on last char
            idx_s1 += 1  # move to next character in str1

        if contains_substr:  # if we know a substring exists, find min substring
            if str1[start] == str2[idx_s2]:  # if characters match, decrement s2 pointer
                idx_s2 -= 1
                if idx_s2 < 0:  # found the start of the substring
                    # if there's no min substring, or it's less than previous, set new min substring
                    if len(min_substr) == 0 or end - start < len(min_substr):
                        min_substr = str1[start:end]
                        contains_substr = False
            start -= 1

    return min_substr
