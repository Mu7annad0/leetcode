from collections import defaultdict


def findMatrix(nums):
    counter = defaultdict(int)
    res = []

    for num in nums:
        row = counter[num]
        if len(res) == row:
            res.append([])
        res[row].append(num)
        counter[num] += 1

    return res


if __name__ == "__main__":
    nums = [1, 3, 4, 1, 2, 3, 1]
    print(findMatrix(nums))
