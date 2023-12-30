def transpose_matrix(mtrx):
    print("this gives us the length of the mtrx row wise: " + str(len(mtrx)))
    print("this gives us the length of the mtrx column wise: " + str(len(mtrx[0])))
    transposed_mtrx = []

    for column_index in range(len(mtrx[0])):
        new_row_to_add = []
        for row_index in range(len(mtrx)):
            new_row_to_add.append(mtrx[row_index][column_index])
        transposed_mtrx.append(new_row_to_add)

    return transposed_mtrx


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6]]
    t_mtrx = transpose_matrix(matrix)
    print(t_mtrx)
