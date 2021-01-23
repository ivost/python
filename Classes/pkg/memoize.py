import functools
import time


@functools.lru_cache(maxsize=2)
def func(x):
    print(f"**** func({x}) executing for 1 sec")
    time.sleep(1)
    return x * 10


def func2(x):
    time.sleep(1)
    print(f"=== func2 {x}")
    return x * 10


def sum3(x, y, z):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    return x + y + z


if __name__ == '__main__':

    [print(f"func({x}) = {func(x)}") for x in [1, 2, 2, 1, 3, 3, 1]]

    # or
    cached_func = functools.lru_cache()(func2)

    for x in [1, 2, 1]:
        print(f"func({x}) = {cached_func(x)}")

    print(f"result of sum3 {sum3(1, 2, 3)}")

    sum2 = functools.partial(sum3, z=0)
    sum1 = functools.partial(sum2, y=1)
    print(f"result of sum2 {sum2(1, 2)}")
    print(f"result of sum1 {sum1(1)}")

    area = lambda x: x[0] * x[1]

    sum2l = lambda a, b: sum3(a, b, 0)
    print(f"result of sum2l {sum2l(1, 2)}")

    p = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]

    q = sorted(p, key=lambda x: x[0] * x[1])
    print("sorted by product of elements", q)
