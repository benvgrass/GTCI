def find_max_sliding_window(nums, w):
    window = OrderedList(nums[:w])
    max_windows = [window.max()]
    i = 0
    while i + w < len(nums):
        max_windows.append(window.slide_and_max(nums[i], nums[i+w]))
        i += 1
    return max_windows


class OrderedList:
    def __init__(self, nums):
        self.window = []
        for num in nums:
            self.__insert(num)

    def __insert(self, num):
        inserted = False
        i = 0
        while i < len(self.window) and not inserted:
            if num > self.window[i]:
                self.window.insert(i, num)
                inserted = True
            i += 1
        if not inserted:
            self.window.append(num)

    def __remove(self, num):
        assert num in self.window
        self.window.remove(num)

    def slide_and_max(self, old_num, new_num):
        self.__remove(old_num)
        self.__insert(new_num)
        return self.max()

    def max(self):
        return self.window[0]
