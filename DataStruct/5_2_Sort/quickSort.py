def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    return right_mark


if __name__ == '__main__':
    alist = [54, 17, 26, 38, 93, 57, 31]
    quick_sort(alist)
    print(alist)