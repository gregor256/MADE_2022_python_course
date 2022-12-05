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

    def __call__(self, *args, **kwargs):
        """FuncWithStat"""
        return self.namely_function(*args, **kwargs)

    def print_stat(self):
        """FuncWithStat"""
        string_io = io.StringIO()
        sort_by = 'cumulative'
        p_stats = pstats.Stats(profiler, stream=string_io).sort_stats(sort_by)
        p_stats.print_stats()
        funcs = string_io.getvalue().split('\n')
        for line, function_stats in enumerate(funcs):
            if line == 4 or re.search(rf'\({self.namely_function.__name__}\)', function_stats):
                print(function_stats)


def profile_deco(function):
    """profile_deco"""
    wrapper = FuncWithStat(function)
    return wrapper


@profile_deco
def add(arg1, arg2):
    """add"""
    return arg1 + arg2


@profile_deco
def no_add():
    """no_add"""
    return 0


@profile_deco
def sub(arg1, arg2):
    """sub"""
    return arg1 - arg2


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    print(add(1, 2))
    print(add(1, 2))
    print(add(1, 2))
    print(no_add())
    print(no_add())
    print(no_add())
    add.print_stat()

    profiler.disable()
