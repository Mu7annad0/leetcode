def maxWidthOfVerticalArea(points):
    points.sort()
    width = 0

    for i in range(len(points) - 1):
        width = max(width, (points[i + 1][0] - points[i][0]))

    return width


if __name__ == "__main__":
    prices = [[8, 7], [9, 9], [7, 4], [9, 7]]

    print(maxWidthOfVerticalArea(prices))
