def closest(array):
    """Get numbers closest to zero"""
    if not array:
        return []
    res = []
    for element in array:
        if not res:
            res.append(element)
        else:
            if abs(element) < abs(res[0]):
                res = [element]
            elif abs(element) > abs(res[0]):
                continue
            else:
                res.append(element)
    return res


assert closest([-1, 2, -5, 1, -1]) == [-1, 1, -1]
assert closest([-1, 2, -5, 1]) == [-1, 1]
assert closest([]) == []
assert closest([-1, 2, -5, 1, 0]) == [0]
assert closest([10000, -99999]) == [10000]
assert closest([1 - 2 * (i % 2) for i in range(10)]) == [1 - 2 * (i % 2) for i in range(10)]  # [-1 ,1, -1, 1, ...]
print('OK')
