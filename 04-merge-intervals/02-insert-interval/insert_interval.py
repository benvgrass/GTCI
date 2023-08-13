def insert_interval(existing_intervals, new_interval):
    new_schedule = []
    interval_index = 0

    # search for place to put new interval
    while interval_index < len(existing_intervals) and not new_interval.start > existing_intervals[interval_index]:
        new_schedule.append(existing_intervals[interval_index])
        interval_index += 1

    # check for overlap with last interval

    # check for overlap with


    return []


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
