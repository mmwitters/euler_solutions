from functools import lru_cache

@lru_cache(maxsize=None)
def num_of_paths(x, y):
    if y > x:
        return num_of_paths(y, x)
    if x == 0 or y == 0:
        return 1
    elif x == 0:
        return num_of_paths(x, y - 1)
    elif y == 0:
        return num_of_paths(x - 1, y)
    return num_of_paths(x - 1, y) + num_of_paths(x, y - 1)

print(num_of_paths(20, 20))

