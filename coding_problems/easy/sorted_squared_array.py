def sorted_squared_array(array):
    right = 0
    left = len(array) - 1
    sq_array = [0] * len(array)
    sq_array_index = len(array) - 1

    for sq_array_index in reversed(range(0, len(sq_array))):
        right_side_sq = abs(array[right]) * abs(array[right])
        left_side_sq = abs(array[left]) * abs(array[left])
        if right_side_sq < left_side_sq:
            sq_array[sq_array_index] = left_side_sq
            left -= 1
        else:
            sq_array[sq_array_index] = right_side_sq
            right += 1

    return sq_array


if __name__ == '__main__':
    # array = [1, 2, 3, 5, 6, 8, 9]
    array = [-5, -4, -3, -2, -1]
    sq = sorted_squared_array(array)
    print(sq)
