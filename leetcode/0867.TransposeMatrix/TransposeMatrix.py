def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    res = [[0] * rows for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            res[c][r] = matrix[r][c]

    return res


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(matrix))
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
