def matrix_addition(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

mat1 = [[1, 2], [5, 3]]
mat2 = [[2, 3], [4, 1]]

mat_sum = matrix_addition(mat1, mat2)

print("Mat Sum =")
for row in mat_sum:
    print(" ".join(map(str, row)))
