from n04_merge_intervals.interval import Interval


def insert_interval(existing_intervals, new_interval):
    new_schedule = []
    interval_index = 0

    existing_count = len(existing_intervals)

    # search for place to put new interval
    while interval_index < existing_count and new_interval.start > existing_intervals[interval_index].start:
        new_schedule.append(existing_intervals[interval_index])
        interval_index += 1

    # check for overlap with last interval
    next_interval = new_interval
    if interval_index > 0 and new_schedule[-1].end >= new_interval.start:
        last_interval = new_schedule.pop()
        next_interval = Interval(last_interval.start, max(new_interval.end, last_interval.end))

    # check for overlap with remaining intervals and use it to create the next interval
    # stop looping when there's no more overlap
    while interval_index < existing_count and next_interval.end >= existing_intervals[interval_index].start:
        next_interval = Interval(next_interval.start, max(next_interval.end, existing_intervals[interval_index].end))
        interval_index += 1
    new_schedule.append(next_interval)

    for interval in existing_intervals[interval_index:]:
        new_schedule.append(interval)

    return new_schedule
