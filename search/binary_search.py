import random
from typing import List, NewType

from sort.quick_sort import quick_sort_v2

IndexNum = NewType('IndexNum', int)


# def linear_search(n: List[int], value: int) -> IndexNum:
#     for i in range(0, len(n)):
#         if n[i] == value:
#             return i
#     return -1


# def binary_search(n: List[int], value: int) -> IndexNum:
#     left, right = 0, len(n) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if n[mid] == value:
#             return mid
#         elif n[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

def binary_search(n: List[int], value: int) -> IndexNum:
    def _binary_search(n: List[int], value: int,
                       left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1

        mid = (left + right) // 2
        if n[mid] == value:
            return mid
        elif n[mid] < value:
            return _binary_search(n, value, mid + 1, right)
        else:
            return _binary_search(n, value, left, mid - 1)

    return _binary_search(n, value, 0, len(n) - 1)


if __name__ == '__main__':
    nums = [random.randint(0, 100) for i in range(8)] + [11]
    sort_nums = quick_sort_v2(nums)
    print(sort_nums)
    print(binary_search(sort_nums, 11))