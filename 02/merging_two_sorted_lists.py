def merge(array_1, array_2):
    """Merging two sorted arrays. Delete duplicates. Each element in result should exist in every array"""
    length_1 = len(array_1)
    length_2 = len(array_2)
    merged = []
    max_appended = 0
    i, j = 0, 0
    while i < length_1 and j < length_2:
        if array_1[i] == array_2[j]:
            if not merged or array_1[i] != max_appended:
                merged.append(array_1[i])
                max_appended = array_1[i]
            i += 1
            j += 1
        elif array_2[j] < array_1[i]:
            j += 1
        else:
            i += 1

    return merged


assert merge([], (1, 1, 2, 3, 4, 7)) == []
assert merge([1, 1, 2, 5, 7], []) == []
assert merge([], ()) == []
assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]
assert merge([1, 1, 1, 1, 1], [-1, 1, 1, 1, 1, 1]) == [1]
assert merge([1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]) == [1]
