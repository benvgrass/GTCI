def find_max_sliding_window(nums, w):
    window = ArrayWindowSlider(w, nums)
    max_windows = [window.max()]
    i = 0
    while i + w < len(nums):
        max_windows.append(window.slide_max(i+w, i+1))
        i += 1
    return max_windows


class ArrayWindowSlider:
    def __init__(self, w, nums):
        self.window = []
        self.num_ref = nums
        for idx in range(w):
            self.__insert(idx)

    def __insert(self, idx):
        num = self.num_ref[idx]
        i = 0
        while i < len(self.window) and num < self.num_ref[self.window[i]]:
            i += 1
        del self.window[i:]
        self.window.append(idx)

    def slide_max(self, new_idx, least_index):
        self.__insert(new_idx)
        return self.max(least_index)

    def max(self, least_index=0):
        while self.window[0] < least_index:
            del self.window[0]
        return self.num_ref[self.window[0]]

