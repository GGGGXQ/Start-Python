# O(nlogn)需要把切片操作改成传入头尾下标
def merge_sort(alist):
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k = k + 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
    print("Merging", alist)


# 不使用切片操作的归并排序
def new_merge_sort(alist, start=0, end=None):
    if end is None:
        end = len(alist)
    print("Splitting", alist)
    if start < end - 1:
        mid = (start + end) // 2
        new_merge_sort(alist, start, mid)
        new_merge_sort(alist, mid, end)

        i = start
        j = mid
        k = start
        while i < mid and j < end:
            if alist[i] < alist[j]:
                alist[k] = alist[i]
                i += 1
            else:
                alist[k] = alist[j]
                j += 1
            k += 1

        while i < mid:
            alist[k] = alist[i]
            i += 1
            k += 1
        while j < end:
            alist[k] = alist[j]
            j += 1
            k += 1
    print("Merging", alist)



if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(alist)
    print("------------------------------")
    new_merge_sort(alist)
