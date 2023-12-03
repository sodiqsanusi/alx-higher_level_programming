#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for arr in matrix:
        last_ind = len(arr) - 1
        for elem in arr:
            if elem == arr[last_ind]:
                print("{:d}".format(elem), end='')
                continue
            print("{:d}".format(elem), end=' ')
        print()
