class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

        # set the flag for closed/open

    def __eq__(self, other):
        return isinstance(other, Interval) and other.start == self.start and other.end == self.end

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
            "(" + str(self.start) + ", " + str(self.end) + ")"


def make_interval_list(l):
    return [Interval(x[0], x[1]) for x in l]


def unpack_interval_list(l):
    return [[x.start, x.end] for x in l]
