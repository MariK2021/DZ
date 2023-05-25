def cache_data(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            return result
    return wrapper


@cache_data
def add(a, b):
    return a+b


print(add(3, 7))
print(add(3, 7))
print(add(1, 7))
print(add(1, 7))
