def intervals_intersection(interval_list_a, interval_list_b):
    # Replace this placeholder return statement with your code

    return []


def get_intersection(interval_a, interval_b):
    """
    get_intersection calculates the intersection between two intervals

    :param interval_a: first interval
    :param interval_b: second interval
    :return: intersecting interval of interval_a and interval_b or None if no intersection
    """
    if (interval_b.start <= interval_a.start <= interval_b.end or
            interval_a.start <= interval_b.start <= interval_a.end):
        return Interval(max(interval_a.start, interval_b.start),
                        min(interval_a.end, interval_b.end))

    return None


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
