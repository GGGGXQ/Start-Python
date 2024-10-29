def orderedSequentialSearch(arr, target):
    pos = 0
    found = False
    stop = False
    while pos < len(arr) and not found and not stop:
        if arr[pos] is target:
            found = True
        elif arr[pos] > target:
            stop = True
        else:
            pos = pos + 1
    return found
