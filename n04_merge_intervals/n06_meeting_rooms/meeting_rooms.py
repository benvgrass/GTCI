from n04_merge_intervals.interval import Interval
from heapq import heapreplace, heappush


def find_sets(intervals: list[Interval]):

    intervals.sort(key=lambda i: i.start, reverse=True)  # sort intervals by start time
    meeting_rooms = [intervals.pop()]

    #  iterate while intervals remain in list
    while intervals:
        next_meeting = intervals.pop()  # next meeting to find a room for

        # if there's an open room (start is after earliest ending meeting)
        if next_meeting.start >= meeting_rooms[0]:
            heapreplace(meeting_rooms, next_meeting.end)  # remove last meeting from rooms, add current one
        else:  # otherwise add a new room
            heappush(meeting_rooms, next_meeting.end)

    # size of heap is number of meeting rooms
    return len(meeting_rooms)
