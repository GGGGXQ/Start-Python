import time
import random
from generic_search import linear_contains, binary_contains


def time_search(func, arr, target):
    start_time = time.time()
    result = func(arr, target)
    end_time = time.time()
    return result, end_time - start_time


if __name__ == '__main__':
    numbers = [random.randint(0, 1000000) for _ in range(1000000)]
    targets = [random.randint(0, 1000000) for _ in range(5)]

#   线性查找
    print("linear Searching:")
    for target in targets:
        index, time_taken = time_search(linear_contains, numbers, target)
        print(f"Target {target}: Index = {index} , Time taken = {time_taken:.6f} seconds")

#   二分查找
    print("binary Searching:")
    sort_numbers = sorted(numbers)
    for target in targets:
        index, time_taken = time_search(binary_contains, sort_numbers, target)
        print(f"Target {target}: Index = {index}, Time taken = {time_taken:.6f} seconds")
