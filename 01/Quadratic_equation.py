import math


def solve_equation(a, b, c, verbose=False):
    if math.isclose(a, 0, abs_tol=1.0e-10):
        if math.isclose(b, 0, abs_tol=1.0e-10):
            if math.isclose(c, 0, abs_tol=1.0e-10):
                if verbose:
                    # every real number could be a solution
                    print("\U00002200x\U00002208\U0000211D")
                return 0, 0
            else:
                return
        else:
            return -c / b, -c / b
    else:
        d = b * b - 4 * (a * c)
        if math.isclose(d, 0, abs_tol=1.0e-10) or d > 0:
            return (-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)


def check_solution(solution_function, coefficients):
    a, b, c = coefficients
    d = b * b - 4 * (a * c)
    solution = solution_function(a, b, c)
    # D < 0 or (0, 0, 0)
    if (not math.isclose(d, 0, abs_tol=1.0e-10) and d < 0) or\
            (math.isclose(a, 0, abs_tol=1.0e-10) and
             math.isclose(b, 0, abs_tol=1.0e-10) and
             not math.isclose(c, 0, abs_tol=1.0e-10)):
        return solution is None
    # x1 and x2 into equation
    else:
        x1, x2 = solution
        return math.isclose(a * x1 * x1 + b * x1 + c, 0, abs_tol=1.0e-10) and\
               math.isclose(a * x2 * x2 + b * x2 + c, 0, abs_tol=1.0e-10)


assert check_solution(solve_equation, (0, 0, 0))
assert check_solution(solve_equation, (0, 0, 10))
assert check_solution(solve_equation, (0, 10, 10))

assert check_solution(solve_equation, (1, 2, 1))
assert check_solution(solve_equation, (1, 2.0001, 1))

assert check_solution(solve_equation, (3, 20, 1))
assert check_solution(solve_equation, (42, 420, 42))
assert check_solution(solve_equation, (-42, 420, 42))
assert check_solution(solve_equation, (-42, -420, 42))
assert check_solution(solve_equation, (-42, 420, -42))

print('OK')
