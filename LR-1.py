import time
from functools import wraps

EX_1 = [1, [2, 3], 2]
EX_2 = [1, [2, [3, 2]], 1]
EX_3 = ['a', ['b', ['a', ['c', 'b']]], 'a']
EX_4 = [0, [1, [2, [3, [4, {}, 3, []]]], ''], None, 0]

def func_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            resultTime = time.perf_counter() - start
            print(f"{func.__name__}: {resultTime:.6f} с")
    return wrapper
# 1
from collections.abc import Sized


def is_empty(item) -> bool:
    return item is None or (isinstance(item, Sized) and len(item) == 0)

@func_time
def flatten(items: list) -> list:
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif not is_empty(item):
            result.append(item)
    return result

print("1 Задание:")
print(flatten(EX_1))
print(flatten(EX_2))
print(flatten(EX_3))
print(flatten(EX_4))
# 2
@func_time
def count_items(items: list) -> dict:
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


print("2 Задание:")
print(count_items(flatten(EX_1)))
print(count_items(flatten(EX_2)))
print(count_items(flatten(EX_3)))
print(count_items(flatten(EX_4)))