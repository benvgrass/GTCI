from collections import Counter


def least_time(tasks, n):
    wait_time = 0
    counts = list(Counter(tasks).values()).sort(reverse=True)
    while counts:
        wait_time += max(0, n - len(counts))
        counts = [x - 1 for x in counts if x - 1 > 0]

    return wait_time + len(tasks)
