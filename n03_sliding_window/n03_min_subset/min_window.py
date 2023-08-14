def min_window(str1, str2):
    idx_s1 = 0
    idx_s2 = 0
    min_substr = ''
    start = 0
    end = 0

    while idx_s1 < len(str1):  # iterate through s1. when done with s1 we return substring
        if str1[idx_s1] == str2[idx_s2]:  # if characters match, move to next character in str2
            idx_s2 += 1
            if idx_s2 >= len(str2):
                contains_substr = True
                start, end = idx_s1, idx_s1 + 1  # initialize backtrack loop variables

                idx_s2 -= 1  # move str2 pointer to last char of s2
                while idx_s2 >= 0:
                    if str1[start] == str2[idx_s2]:  # if characters match, decrement s2 pointer
                        idx_s2 -= 1
                    start -= 1
                start += 1
                if len(min_substr) == 0 or end - start < len(min_substr):
                    min_substr = str1[start:end]
                idx_s2 = 0
        idx_s1 += 1  # move to next character in str1

    return min_substr
