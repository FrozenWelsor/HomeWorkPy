EX_1 = [1, [2, 3], 2]
EX_2 = [1, [2, [3, 2]], 1]
EX_3 = ['a', ['b', ['a', ['c', 'b']]], 'a']
EX_4 = [0, [1, [2, [3, [4, {}, 3, []]]], ''], None, 0]

# 1
from collections.abc import Sized


def is_empty(item) -> bool:
    return item is None or (isinstance(item, Sized) and len(item) == 0)


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