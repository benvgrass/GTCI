from collections import Counter


def least_time(tasks, n):
    counts = list(Counter(tasks).values())  # get list of counts of each character
    counts.sort()  # sort them (ascending order because we use <list>.pop() which takes from end
    max_count = counts.pop()  # pop max count off list

    # initialize max time as n(count-1) which is idle time if there's only one character
    wait_time = (max_count - 1) * n

    # iterate through count of each character
    while counts:
        current_count = counts.pop()  # pop next most frequent count
        wait_time -= min(current_count, max_count-1)  # subtract number of wait spots that would be filled

    # if negative this means that there are more tasks than wait time so that every spot was filled therefore
    # there's no idle time. that plus 1 unit per task (ie # of tasks ie len tasks) is the min time
    wait_time = max(0, wait_time)
    return wait_time + len(tasks)
