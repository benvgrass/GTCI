from heapq import heappop, heappush
from n04_merge_intervals.interval import Interval


def employee_free_time(schedule):
    result = []  # free interval list
    interval_heap = []  # heap of tuples (<start_time>, <employee_index>)

    def push_next_interval(employee_index):
        """
        pops next interval from employee list and adds to heap

        :param employee_index: index of employee
        """
        employee_times = schedule[employee_index]
        if employee_times:
            employee_interval = employee_times.pop(0)
            start = employee_interval.start
            end = employee_interval.end
            heappush(interval_heap, (start, end, i))

    # initialize heap with first interval for each employee
    for i in range(len(schedule)):
        push_next_interval(i)

    # initialize last_end_time to be start of first interval
    last_end_time = interval_heap[0][0]
    # iterate over heaps selecting the next soonest interval until there are no more appointments
    while interval_heap:
        start_time, end_time, employee = heappop(interval_heap)  # pop next starting event

        if start_time > last_end_time:  # if there's space between the last event that ended and this one, it's free
            result.append(Interval(last_end_time, start_time))

        if end_time > last_end_time:  # update next free time if event is new last ending event
            last_end_time = end_time

        push_next_interval(employee)  # add next event for this employee to heap

    return result
