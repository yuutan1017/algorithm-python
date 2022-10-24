import random
from typing import List


def bubble_sort(n: List[int]) -> List[int]:
    for i in range(len(n)):
        for j in range(len(n) - 1 - i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(10)]
    print(bubble_sort(nums))