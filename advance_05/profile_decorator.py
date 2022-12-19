"""profile"""
import cProfile
import io
import pstats
import re


class FuncWithStat:
    """FuncWithStat"""

    def __init__(self, function):
        """FuncWithStat"""
        self.namely_function = function
        self.profiler = cProfile.Profile()

    def __call__(self, *args, **kwargs):
        """FuncWithStat"""
        self.profiler.enable()
        result = self.namely_function(*args, **kwargs)
        self.profiler.disable()
        return result

    def print_stat(self):
        """FuncWithStat"""
        string_io = io.StringIO()
        sort_by = 'cumulative'
        p_stats = pstats.Stats(self.profiler, stream=string_io).sort_stats(sort_by)
        p_stats.print_stats()
        funcs = string_io.getvalue().split('\n')
        print(f'{self.namely_function.__name__} function stats: ')
        for line, function_stats in enumerate(funcs):
            if line == 4 or re.search(rf'\({self.namely_function.__name__}\)', function_stats):
                print(function_stats)
        print()


def profile_deco(function):
    """profile_deco"""
    wrapper = FuncWithStat(function)
    return wrapper


@profile_deco
def add(arg1, arg2):
    """add"""
    return arg1 + arg2


@profile_deco
def sub(arg1, arg2):
    """sub"""
    return arg1 - arg2


@profile_deco
def no_add():
    """no_add"""
    return 0


if __name__ == '__main__':
    print(add(1, 2))
    print(add(1, 2))
    print(add(1, 2))
    print(sub(1, 2))
    print(sub(1, 2))
    print(no_add())
    print(no_add())
    print(no_add())
    add.print_stat()
    sub.print_stat()
