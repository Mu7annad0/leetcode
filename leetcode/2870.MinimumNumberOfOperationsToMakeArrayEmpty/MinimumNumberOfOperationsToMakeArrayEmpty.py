import math
from collections import Counter


def minOperations(nums):

    operations = 0
    counter = Counter(nums)

    for num in counter.values():
        if num == 1:
            return -1
        """operations += num // 3
        if num % 3:
            operations += 1"""
        operations += math.ceil(num / 3)

    return operations



if __name__ == "__main__":

    nums = [2,3,3,2,2,4,2,3,4]

    print(minOperations(nums))



