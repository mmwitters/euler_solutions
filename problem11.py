f = open("11.txt", "r")
lines = f.readlines()
parsed_lines = map(lambda line: line.strip().split(" "),
                   lines)
int_lines = list(map(lambda line: list(map(lambda numstr: int(numstr), line)), parsed_lines))
print(int_lines)


def row(matrix):
    largest_product = 0
    for row in matrix:
        for i in range(len(row) - 3):
            current_product = row[i] * row[i + 1] * row[i + 2] * row[i + 3]
            if current_product > largest_product:
                largest_product = current_product
    return largest_product


def column(matrix):
    largest_product = 0
    length = len(matrix[0])
    for i in range(length):
        for j in range(len(matrix) - 3):
            current_product = matrix[j][i] * matrix[j + 1][i] * matrix[j + 2][i] * matrix[j + 3][i]
            if current_product > largest_product:
                largest_product = current_product
    return largest_product


def descending_diagonal(matrix):
    largest_product = 0

    height = len(matrix)
    width = len(matrix[0])
    for row in range(height - 3):
        for col in range(width - 3):
            current_product = matrix[row][col] \
                              * matrix[row + 1][col + 1] \
                              * matrix[row + 2][col + 2] \
                              * matrix[row + 3][col + 3]
            if current_product > largest_product:
                largest_product = current_product
    return largest_product


def ascending_diagonal(matrix):
    largest_product = 0

    height = len(matrix)
    width = len(matrix[0])
    for row in range(height - 3):
        for col in range(3, width):
            current_product = matrix[row][col] \
                              * matrix[row + 1][col - 1] \
                              * matrix[row + 2][col - 2] \
                              * matrix[row + 3][col - 3]
            if current_product > largest_product:
                largest_product = current_product
    return largest_product


def find_largest(matrix):
    row_rsl = row(matrix)
    column_rsl = column(matrix)
    desc = descending_diagonal(matrix)
    asc = ascending_diagonal(matrix)
    return max([row_rsl, column_rsl, desc, asc])

print(find_largest(int_lines))