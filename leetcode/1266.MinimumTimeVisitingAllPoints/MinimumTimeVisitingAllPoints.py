def minTimeToVisitAllPoints(points):
    """
    The minTimeToVisitAllPoints function calculates the minimum time required to visit a sequence of 2D points.
    It iterates through the points, starting from the second one, and accumulates the maximum absolute differences in x and y coordinates between consecutive points.
    The sum of these differences represents the minimum time needed to traverse the entire sequence of points.
    The function returns this total minimum time.
    """
    res = 0

    for i in range(1, len(points)):
        res += max(abs(points[i][0] - points[i - 1][0]),
                   abs(points[i][1] - points[i - 1][1]))

    return res


if __name__ == '__main__':
    points = [[1, 1], [3, 4], [-1, 0]]
    print(minTimeToVisitAllPoints(points))
    # 7
