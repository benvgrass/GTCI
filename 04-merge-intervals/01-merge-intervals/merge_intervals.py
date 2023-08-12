def merge_intervals(intervals):
    # Replace this placeholder return statement with your code
    result = [intervals.pop()]
    for interval in intervals:
        last_interval = result[-1]
        if last_interval.end >= interval.start:
            result[-1] = Interval(result[-1].start, max(result[-1].end, interval.end))

    return result


# from educative.io starter code
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
            "(" + str(self.start) + ", " + str(self.end) + ")"
