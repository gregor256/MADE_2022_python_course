"""Count avg last N runs time"""
import time


def counting(iters_num):
    """Count avg last N runs time"""
    def counting_decorator(function):
        cnt = 0
        queue = []

        def counting_wrapper(*args, **kwargs):
            nonlocal queue
            if len(queue) >= iters_num:
                queue.pop(0)
            start = time.time()
            result = function(*args, **kwargs)
            queue.append(time.time() - start)
            nonlocal cnt
            if cnt < iters_num:
                cnt += 1
            print(f'Average execution time of {function.__name__} in last {cnt}'
                  f' runs is {sum(queue) / cnt}')
            return result
        return counting_wrapper
    return counting_decorator
