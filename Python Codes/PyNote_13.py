def max_in_list(items):
    max = items[0]
    for i in range(1, len(items), 1):
        if items[i] > max:
            max = items[i]

    return max
