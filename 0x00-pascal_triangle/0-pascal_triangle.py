#!/usr/bin/python3
'''
0x00. Pascal's Triangle
'''

def pascal_triangle(n):
    """
    This function returns a triangle
    """

    if n <= 0:
        return []
    pascal_triangle = [[1]]
    for i in range(1, n):
        previous_row = pascal_triangle[-1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(previous_row[j-1] + previous_row[j])
        current_row.append(1)
        pascal_triangle.append(current_row)
    return pascal_triangle
