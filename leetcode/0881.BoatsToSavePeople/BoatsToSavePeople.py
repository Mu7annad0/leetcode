def numRescueBoats(people, limit):
    result = 0
    l, r = 0, len(people) - 1
    people.sort()
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        result += 1
    return result


if __name__ == '__main__':
    p = [3, 2, 2, 1]
    l = 3
    print(numRescueBoats(p, l))
