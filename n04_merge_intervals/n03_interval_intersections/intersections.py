from n04_merge_intervals.interval import Interval


def intervals_intersection(interval_list_a, interval_list_b):
    result = []
    a_index = 0
    b_index = 0
    len_a = len(interval_list_a)
    len_b = len(interval_list_b)

    while a_index < len_a and b_index < len_b:
        current_interval_a = interval_list_a[a_index]
        current_interval_b = interval_list_b[b_index]
        next_intersection = get_intersection(current_interval_a,
                                             current_interval_b)
        if next_intersection:
            result.append(next_intersection)

        if current_interval_a.end < current_interval_b.end:
            a_index += 1
        else:
            b_index += 1

    return result


def get_intersection(interval_a, interval_b):
    """
    get_intersection calculates the intersection between two intervals

    :param interval_a: first interval
    :param interval_b: second interval
    :return: intersecting interval of interval_a and interval_b or None if no intersection
    """
    start = max(interval_a.start, interval_b.start)
    end = min(interval_a.end, interval_b.end)

    if start <= end:
        return Interval(start, end)

    return None
