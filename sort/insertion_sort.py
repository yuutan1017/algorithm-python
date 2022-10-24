import random
from typing import List


def insertion_sort(n: List[int]) -> List[int]:
    for i in range(1, len(n)):
        temp = n[i]
        j = i - 1
        while j >= 0 and n[j] > temp:
            n[j+1] = n[j]
            j -= 1

        n[j+1] = temp

    return n


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(10)]
    print(insertion_sort(nums))