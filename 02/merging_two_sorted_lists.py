def merge(array_1, array_2):
    """Merging two sorted arrays"""
    length_1 = len(array_1)
    length_2 = len(array_2)
    merged = []
    i, j = 0, 0
    while i < length_1 or j < length_2:
        if i == length_1 or (j < length_2 and array_1[i] >= array_2[j]):
            if not merged or (merged and merged[-1] != array_2[j]):
                merged.append(array_2[j])
            j += 1
        else:
            if not merged or (merged[-1] != array_1[i]):
                merged.append(array_1[i])
            i += 1
    return merged


assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 3, 4, 5, 7]
assert merge([], (1, 1, 2, 3, 4, 7)) == [1, 2, 3, 4, 7]
assert merge([1, 1, 2, 5, 7], []) == [1, 2, 5, 7]
assert merge([1, 1, 1, 1, 1], [-1, 1, 1, 1, 1, 1]) == [-1, 1]
assert merge([1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]) == [1]
assert merge([], ()) == []
print('OK')
