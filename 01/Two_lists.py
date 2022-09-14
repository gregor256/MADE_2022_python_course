def get_two_lists(input_list):
    odd, even = [], []
    for element in input_list:
        if element % 2:
            odd.append(element)
        else:
            even.append(element)
    return even, odd


assert get_two_lists([i for i in range(-5, 5)]) == ([-4, -2, 0, 2, 4], [-5, -3, -1, 1, 3])
assert get_two_lists([0 for i in range(-5, 5)]) == ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [])
assert get_two_lists([-1 for i in range(-5, 5)]) == ([], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
print('OK')
