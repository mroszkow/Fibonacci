def fib_seq_item(n: int) -> int:
    fibonacci_numbers = []
    one_step_back = 1
    two_step_back = 0
    for i in range(n + 1):
        if i in (0, 1):
            item = i
        elif i > 1:
            item = one_step_back + two_step_back
            two_step_back, one_step_back = one_step_back, item

        fibonacci_numbers.append(item)

    return fibonacci_numbers


if __name__ == "__main__":
    print(fib_seq_item(19))
