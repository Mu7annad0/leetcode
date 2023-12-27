def numRollsToTarget(n, k, target):

    MOD = 10 ** 9 + 7
    cashe = {}

    def count(n, target):

        if n == 0:
            return 1 if target == 0 else 0

        if (n, target) in cashe:
            return cashe[(n, target)]

        res = 0
        for val in range(1, k + 1):
            res = (res + count(n - 1, target - val)) % MOD

        cashe[(n, target)] = res
        return res

    return count(n, target)

if __name__ == "__main__":
    target = 7
    n = 2
    k = 6
    print(numRollsToTarget(n, k, target))
    # 6
