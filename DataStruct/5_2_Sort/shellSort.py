# O(n**2)
def shell_sort(alist):
    sub_list_count = len(alist) // 2
    while sub_list_count > 0:
        for start_position in range(sub_list_count):
            gap_insertion_sort(alist, start_position, sub_list_count)
        print("After increments of size", sub_list_count, "The list is", alist)
        sub_list_count = sub_list_count // 2


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = current_value


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 78, 50, 34, 92]
    shell_sort(alist)