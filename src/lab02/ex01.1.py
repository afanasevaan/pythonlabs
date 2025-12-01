def min_max(nums: list[float | int]):
    if not nums:
        raise TypeError("Value Error")
    else:
        return min(nums), max(nums)


print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))
