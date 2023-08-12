def merge_intervals(intervals):
    # Replace this placeholder return statement with your code
    result = [intervals.pop(0)]
    for interval in intervals:
        last_interval = result[-1]
        if last_interval.end >= interval.start:
            result[-1] = Interval(last_interval.start, max(last_interval.end, interval.end))
        else:
            result.append(interval)

    return result


# from educative.io starter code
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
