def col_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    len_s = len(mat[0])
    for i in mat:
        if len(i)!= len_s:
            raise TypeError ("ValueError")
    R = []
    for i in range (len(mat[0])):
        sum_s = 0
        for j in range(len(mat)):
            sum_s += mat[j][i]
        R.append(sum_s)
    return R
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
