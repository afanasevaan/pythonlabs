## Лабораторная работа 2

### Задание A1

```
def min_max(nums: list[float | int]):
    if not nums:
        raise TypeError ('Value Error')
    else:
        return min(nums), max(nums)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))


```

![im01.1.png](/images/lab02/im01.1.png)


### Задание A2

```
def unique_sorted(nums: list[float | int]):
    return (list(sorted(set(nums))))
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print(unique_sorted([]))
```

![im01.2.png](/images/lab02/im01.2.png)

### Задание A3

```
def flatten(mat: list[list | tuple]):
    flattened_list =  []
    for row in mat:
        if isinstance(row, (list, tuple)):
            flattened_list.extend(row)
        else:
            raise TypeError ('TypeError')
    return (flattened_list)
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```

![im01.3.png](/images/lab02/im01.3.png)

### Задание B1

```
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
```

![im02.1.png](/images/lab02/im02.1.png)

### Задание B2

```
def row_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    len_s = len(mat[0])
    for i in mat:
        if len(i)!=len_s:
            raise TypeError ("ValueError")
    R = []
    for i in mat:
        R.append(sum(i))
    return R
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```

![im02.2.png](/images/lab02/im02.2.png)

### Задание B3

```
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
```

![im02.3.png](/images/lab02/im02.3.png)

## Лабораторная работа 3
