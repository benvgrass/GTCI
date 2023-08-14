from n04_merge_intervals.interval import Interval


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
