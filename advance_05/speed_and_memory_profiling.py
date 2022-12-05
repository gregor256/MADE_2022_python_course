import time
import weakref
import cProfile
import io
import pstats
from memory_profiler import profile

CONST = 500
INSTANCES_NUM_STORE = int(1e5)
INSTANCES_NUM_GENERATE = int(1e5)
N_ITERS = 20


class FirstDefaultProperty:
    def __init__(self, object_having_property):
        self.object_having_property = object_having_property

    def print_name(self):
        print(self)

    def print_name2(self):
        print(str(self) + str(self))


class SecondDefaultProperty:
    def __init__(self, object_having_property):
        self.object_having_property = object_having_property

    def print_name(self):
        print(self)

    def print_name2(self):
        print(str(self) + str(self))


class FirstWeakRefProperty:
    def __init__(self, object_having_property):
        self.object_having_property = weakref.ref(object_having_property)

    def print_name(self):
        print(self)

    def print_name2(self):
        print(str(self) + str(self))


class SecondWeakRefProperty:
    def __init__(self, object_having_property):
        self.object_having_property = weakref.ref(object_having_property)

    def print_name(self):
        print(self)

    def print_name2(self):
        print(str(self) + str(self))


class DefaultClass:
    def __init__(self, parameter):
        parameter = parameter % 100
        self.name = 'abc'  # * parameter
        self.surname = 'def'  # * (parameter * parameter)
        self.height = parameter * parameter
        self.weight = 2 * parameter
        self.first_property = FirstDefaultProperty(self)
        self.second_property = SecondDefaultProperty(self)

    def add(self):
        return self.weight + self.height

    def add_str(self):
        return self.name + self.surname


class SlotsClass:
    __slots__ = ('name', 'surname',
                 'height', 'weight',
                 'height1', 'weight1',
                 'height2', 'weight2',
                 'height3', 'weight3',
                 'first_property', 'second_property'
                 )

    def __init__(self, parameter):
        parameter = parameter % 100
        self.name = 'abc'  # * parameter
        self.surname = 'def'  # * (parameter * parameter)
        self.height = parameter * parameter
        self.weight = 2 * parameter
        self.first_property = FirstDefaultProperty(self)
        self.second_property = SecondDefaultProperty(self)

    def add(self):
        return self.weight + self.height

    def add_str(self):
        return self.name + self.surname


class WeakRefClass:
    def __init__(self, parameter):
        parameter = parameter % 100
        self.name = 'abc'  # * parameter
        self.surname = 'def'  # * (parameter * parameter)
        self.height = parameter * parameter
        self.weight = 2 * parameter
        self.first_property = FirstWeakRefProperty(self)
        self.second_property = SecondWeakRefProperty(self)

    def add(self):
        return self.weight + self.height

    def add_str(self):
        return self.name + self.surname


def create_instances_pack(some_class):
    class_tuple = tuple(some_class(parameter) for parameter in range(INSTANCES_NUM_STORE))
    return class_tuple


def get_access_to_attributes(some_class):
    name, surname, height, weight = None, None, None, None
    for _ in range(INSTANCES_NUM_GENERATE):
        element = some_class(10)
        name = element.name
        surname = element.surname
        height = element.height
        weight = element.weight
    return name, surname, height, weight


def change_attributes(some_class):
    for _ in range(INSTANCES_NUM_GENERATE):
        element = some_class(10)
        element.name += 'name'
        element.surname += 'surname'
        element.height *= CONST
        element.weight *= CONST


def delete_attributes(instances_pack):
    for instance in instances_pack:
        del instance.name
        del instance.surname
        del instance.height
        del instance.weight
        del instance.first_property
        del instance.second_property


@profile
def get_time(some_class, iters_num):
    class_tuple = ()
    print(some_class.__name__)
    start_time = time.time()
    for _ in range(iters_num):
        class_tuple = create_instances_pack(some_class)
    print('avg creation time:', (time.time() - start_time) / iters_num)

    start_time = time.time()
    for _ in range(iters_num):
        get_access_to_attributes(some_class)

    print('avg access time:', (time.time() - start_time) / iters_num)
    start_time = time.time()
    change_attributes(some_class)
    print('avg change time:', time.time() - start_time)
    start_time = time.time()
    delete_attributes(class_tuple)
    print('delete time:', time.time() - start_time)
    print()


def time_profiler():
    string_io = io.StringIO()
    sort_by = 'cumulative'
    p_stats = pstats.Stats(profiler, stream=string_io).sort_stats(sort_by)
    p_stats.print_stats()
    print(string_io.getvalue())


if __name__ == '__main__':
    profiler = cProfile.Profile()

    profiler.enable()
    get_time(DefaultClass, N_ITERS)
    profiler.disable()
    time_profiler()

    profiler.enable()
    get_time(SlotsClass, N_ITERS)
    profiler.disable()
    time_profiler()

    profiler.enable()
    get_time(WeakRefClass, N_ITERS)
    profiler.disable()
    time_profiler()
