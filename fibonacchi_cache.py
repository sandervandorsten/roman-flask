from functools import wraps


def memoized(func):
    cache = {}

    @wraps(func)
    def impl(n):
        try:
            return_val = cache[n]
        except KeyError:
            return_val = fib(n)
            cache[n] = return_val
        return impl


@memoized
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(5))