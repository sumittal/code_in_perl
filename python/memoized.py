# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def resultcache(f):
    """Result cache decorator"""
    # write your code in Python >= 3.4
    cache = {}
    temp = []

    def memoized_f(*args):
        nonlocal cache
        print("size :", len(cache))
        if len(cache) > 10:
            #cache = {}
            key_to_del = tuple(temp[0])
            print(cache)
            #cache.pop(key_to_del)
            cache.pop((1, 2))
            temp.pop()

        temp.append(args)

        if (args[0], args[1]) in cache:
            return (True, cache[args])
        elif (args[1], args[0]) in cache:
            return (True, cache[tuple(reversed(args))])
        result = f(*args)
        cache[args] = result
        return (False, result)

    return memoized_f


@resultcache
def add_two(a, b):
    return a + b
    
print(add_two(1,2))
print(add_two(2,1))
print(add_two(2,1))

for i in range(10): print(add_two(i,i))

print(add_two(100,-200))
print(add_two(1,2))
print(add_two(1,2))
