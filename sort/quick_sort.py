import random
from typing import List


def partition(n: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = n[high]
    for j in range(low, high):
        if n[j] <= pivot:
            i += 1
            n[i], n[j] = n[j], n[i]

    n[i+1], n[high] = n[high], n[i+1]
    return i+1


def quick_sort(n: List[int]) -> List[int]:
    def _quick_sort(n: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(n, low, high)
            _quick_sort(n, low, partition_index - 1)
            _quick_sort(n, partition_index + 1, high)

    _quick_sort(n, 0, len(n) - 1)
    return n


def quick_sort_v2(data: List[int]) -> List[int]:

    if len(data) <= 1:
        return data

    pivot = data.pop(-1)

    left = [i for i in data if i <= pivot]
    right = [i for i in data if i > pivot]

    left = quick_sort_v2(left)
    right = quick_sort_v2(right)

    return left + [pivot] + right


if __name__ == '__main__':
    nums = [random.randint(0, 100) for i in range(10)]
    print(quick_sort(nums))
    print(quick_sort_v2(nums))
