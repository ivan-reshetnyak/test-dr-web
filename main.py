def fibonacci(num: int):
    if num < 1:
        return

    prev = 1
    cur = 0
    for i in range(1, num + 1):
        yield cur
        temp = cur
        cur = cur + prev
        prev = temp


# https://github.com/ivan-reshetnyak/test-dr-web
# Generator function
def fibonacci_even(num: int):
    if num < 1:
        return []
    if num == 1:
        yield 0
        return

    fn1 = 0
    fn4 = 2
    for i in range(1, num + 1):
        yield fn1
        fn7 = 4 * fn4 + fn1
        fn1 = fn4
        fn4 = fn7


print(fibonacci_even(-1))
print([_ for _ in fibonacci_even(-1)])
print(fibonacci_even(1))
print([_ for _ in fibonacci_even(1)])
print(fibonacci_even(2))
print([_ for _ in fibonacci_even(2)])
print(fibonacci_even(4))
print([_ for _ in fibonacci_even(4)])
print(fibonacci_even(10))
print([_ for _ in fibonacci_even(10)])
