def bubble_sort(alist):
    for pass_num in range(len(alist) - 1, 0, -1):
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# 短冒泡排序
def short_bubble_sort(alist):
    pass_num = len(alist) - 1
    exchanges = True
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        pass_num = pass_num - 1