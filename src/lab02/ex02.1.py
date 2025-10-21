def transpose(mat: list[list[float | int]]):
    if len(mat)==0:
        return []
    len_s = len(mat[0])
    for i in mat:
        if len(i) != len_s:
            raise TypeError ("ValueError")
    R = []
    for i in range(len(mat[0])):
        N = []
        for j in range(len(mat)):
             N.append(mat[j][i])
        R.append(N)
    return R
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1, 2], [3]]))
print(transpose([]))


