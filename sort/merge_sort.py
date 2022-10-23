import random
from typing import List


def merge_sort(n: List[int]) -> List[int]:
    if len(n) <= 1:
        return n

    center = len(n) // 2
    left = n[:center]
    right = n[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            n[k] = left[i]
            i += 1
        else:
            n[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        n[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        n[k] = right[j]
        j += 1
        k += 1

    return n


if __name__ == "__main__":
    nums = [random.randint(0, 100) for i in range(10)]
    print(merge_sort(nums))