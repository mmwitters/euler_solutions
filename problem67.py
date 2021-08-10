triangle = []

f = open("long_triangle.txt", "r")
for line in f:
    new_line = line.split(" ")
    int_list = [int(x) for x in new_line]
    triangle.append(int_list)

for row_index in range(len(triangle) - 2, -1, -1):
    row = triangle[row_index]
    for col_index, num in enumerate(row):
        if num + triangle[row_index + 1][col_index] > num + triangle[row_index + 1][col_index + 1]:
            triangle[row_index][col_index] += triangle[row_index + 1][col_index]
        else:
            triangle[row_index][col_index] += triangle[row_index + 1][col_index + 1]

print(triangle[0][0])