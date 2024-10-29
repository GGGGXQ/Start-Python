def fib3(n:int) -> int:
    if n == 0:
        return 0

    last: int = 0
    next: int = 1
    for _ in range(n):
        last, next, = next, last + next
    return next


if __name__ == "__main__":
    print(fib3(5))
    print(fib3(10))