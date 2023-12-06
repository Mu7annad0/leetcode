def totalMoney(n):

    weeks = n // 7

    low = 28
    high = low + 7 * (weeks - 1)

    res = (weeks * (low + high) // 2)

    for i in range(n % 7):
        res += i + weeks + 1

    return res

def totalMoney2(n):
    weak = total = 0
    day = 1
    total_days = 1
    while total_days <= n:

        if day == 8:
            weak += 1
            day = 1

        total += (day + weak)

        day += 1
        total_days += 1

    return total



if __name__ == "__main__":
    n = 20
    print(totalMoney(n))
    # 96