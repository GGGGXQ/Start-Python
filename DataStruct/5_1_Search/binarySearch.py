def binarySearch(arr, target):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] is target:
            found = True
        else:
            if target < arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# 二分查找的递归版本
def binarySearch2(arr, target):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr) // 2
        if arr[midpoint] is target:
            return True
        else:
            if target < arr[midpoint]:
                return binarySearch2(arr[:midpoint], target)
            else:
                return binarySearch2(arr[midpoint+1:], target)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binarySearch(arr, 10))
    print(binarySearch2(arr, 10))