def fib_rec_item(n: int) -> int:

    if n in (0, 1):
        return n
    else:
        result = fib_rec_item(n - 1) + fib_rec_item(n - 2)
        return result


def fib_rec(m):
    fibonacci_numbers = []
    for i in range(m + 1):
        fibonacci_numbers.append(fib_rec_item(i))
    return fibonacci_numbers


if __name__ == "__main__":
    print(fib_rec_item(19))  # 19th Fibonacci item
    print(fib_rec(19))  # Fibonacci series from 0 to 19 item
