def find_longest_substring(input_str):
    chars = {}
    longest = 0
    start = 0
    end = 0
    len_input = len(input_str)

    while end < len_input and len_input - start > longest:
        c = input_str[end]
        if c in chars:
            new_start = chars[c] + 1
            if new_start > start:
                start = new_start
        chars[c] = end
        end += 1
        if end - start > longest:
            longest = end - start

    return longest
