def numSpecial(mat):
    def get_column_sum(col_idx):
        return sum(row[col_idx] for row in mat)

    special = 0
    for row in mat:
        if sum(row) == 1:
            col_idx = row.index(1)
            special += get_column_sum(col_idx) == 1

    return special

if __name__ == '__main__':
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    # [[1, 0, 0],
    #  [0, 0, 1],
    #  [1, 0, 0]]
    print(numSpecial(mat))
    # 1