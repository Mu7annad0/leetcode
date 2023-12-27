def minCost(colors, neededTime):
    l = total_time = 0

    for r in range(1, len(colors)):
        if colors[r - 1] == colors[r]:
            if neededTime[l] < neededTime[r]:
                total_time += neededTime[l]
                l = r
            else:
                total_time += neededTime[r]
        else:
            l = r
    return total_time


if __name__ == "__main__":
    colors = "aaabbbabbbb"
    neededTime = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]

    print(minCost(colors, neededTime))
