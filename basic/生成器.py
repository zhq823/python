import sys

def fibonacci(n):
    a, b, count = 0, 1, 0
    while True:
        if(count > n):
            return
        yield a
        a, b = b, a + b
        count += 1

maker = fibonacci(10)

while True:
    try:
        print(next(maker))
    except StopIteration:
        sys.exit()