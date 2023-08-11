def min_sub_array_len(target, nums):
    min_len = float("inf")
    win_start = 0
    win_end = 0
    nums_len = len(nums)
    win_sum = 0

    while win_end < nums_len:
        win_sum += nums[win_end]
        win_end += 1

        while win_sum >= target:
            win_len = win_end - win_start
            if win_len < min_len:
                min_len = win_len
            win_sum -= nums[win_start]
            win_start += 1

    if min_len == float("inf"):
        return 0
    return min_len
