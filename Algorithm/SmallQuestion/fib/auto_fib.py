from functools import lru_cache


@lru_cache(maxsize=None)
def fib2(n: int) -> int:
    if n <= 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


if __name__ == "__main__":
    print(fib2(10))
    print(fib2(50))
