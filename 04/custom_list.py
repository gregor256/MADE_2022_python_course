import math


class CustomList(list):
    def __add__(self, other):
        if len(self) > len(other):
            result = self[::]
            for i in range(len(other)):
                result[i] += other[i]
        else:
            result = other[::]
            for i in range(len(self)):
                result[i] += self[i]
        return CustomList(result)

    def __sub__(self, other):
        result = self[::]
        if len(self) > len(other):
            for i in range(len(other)):
                result[i] -= other[i]
        else:
            i = 0
            while i < len(self):
                result[i] -= other[i]
                i += 1
            while i < len(other):
                result.append(-other[i])
                i += 1
        return CustomList(result)

    def __rsub__(self, other):
        return CustomList(other).__sub__(self)

    def __radd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __eq__(self, other):
        return math.isclose(sum(self), sum(other), abs_tol=1.0e-10)

    def __ne__(self, other):
        return not math.isclose(sum(self), sum(other), abs_tol=1.0e-10)

    def __str__(self):
        return '; '.join((' '.join(map(str, self)), str(sum(self))))


# a = CustomList((1, 2, 3, 4, 5))
# b = CustomList((1, 2, 3, 4, 5.00000000001))
# print(a == b)
# print(help(math.isclose))