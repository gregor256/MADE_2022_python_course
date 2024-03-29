import time
from typing import Union


class BaseMetric:
    def __init__(self, function_name: str, metric_name: str):
        self.function_name: str = function_name
        self.metric_name: str = metric_name
        self.parameter: Union[float, int] = 0
        self.start_time: float = 0.0

    def get_name(self) -> str:
        return f'{self.function_name}.{self.metric_name}'

    def get_value(self) -> Union[int, float]:
        return self.parameter

    def add(self, value: Union[float, int] = 0.0) -> None:
        self.update(value)

        Stats.collection[self.get_name()] = self.parameter

    def clear(self) -> None:
        self.parameter = 0.0

    def update(self, value: Union[float, int]) -> None:
        self.parameter += value

    def __enter__(self) -> None:
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.add(time.time() - self.start_time)


class MetricTimer(BaseMetric):
    def __init__(self, name):
        super().__init__(name, 'timer')


class MetricAvg(BaseMetric):
    def __init__(self, name):
        super().__init__(name, 'avg')
        self.count = 0

    def update(self, value: Union[float, int]) -> None:
        total_sum = self.parameter * self.count
        self.parameter = (total_sum + value) / (self.count + 1)
        self.count += 1


class MetricCount(BaseMetric):
    def __init__(self, name):
        super().__init__(name, 'count')

    def update(self, value: Union[float, int]) -> None:
        self.parameter += 1


class Stats:
    instances: dict = {
        'timer': [],
        'avg': [],
        'count': []
    }
    collection: dict = {}

    @classmethod
    def basic_metric_method(cls,
                            metric_class_name: Union[type[MetricCount],
                                                     type[MetricAvg],
                                                     type[MetricTimer]],
                            function_name: str) -> Union[MetricCount,
                                                         MetricAvg,
                                                         MetricTimer]:
        metric_name = metric_class_name('').metric_name
        for instance in cls.instances[metric_name]:
            if instance.get_name() == f'{function_name}.{metric_name}':
                return instance

        new_instance = metric_class_name(function_name)
        cls.instances[metric_name].append(new_instance)
        return new_instance

    @classmethod
    def timer(cls, function_name: str) -> Union[MetricCount, MetricAvg, MetricTimer]:
        return cls.basic_metric_method(MetricTimer, function_name)

    @classmethod
    def avg(cls, function_name: str) -> Union[MetricCount, MetricAvg, MetricTimer]:
        return cls.basic_metric_method(MetricAvg, function_name)

    @classmethod
    def count(cls, function_name) -> Union[MetricCount, MetricAvg, MetricTimer]:
        return cls.basic_metric_method(MetricCount, function_name)

    @classmethod
    def collect(cls) -> dict:
        tmp = cls.collection
        cls.collection: dict = {}
        cls.instances: dict = {
            'timer': [],
            'avg': [],
            'count': []
        }
        return tmp


def calc(same_value: float) -> float:
    return same_value
