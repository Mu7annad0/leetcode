def onesMinusZeros(grid):
    m, n = len(grid), len(grid[0])

    row_ones = [0] * m
    col_ones = [0] * n

    # Count ones in each row and column
    for i in range(m):
        for j in range(n):
            row_ones[i] += grid[i][j]
            col_ones[j] += grid[i][j]

    # Calculate the difference matrix
    for i in range(m):
        for j in range(n):
            grid[i][j] = 2 * (row_ones[i] + col_ones[j]) - m - n

    return grid


if __name__ == '__main__':
    grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
    print(onesMinusZeros(grid))
    # [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]
