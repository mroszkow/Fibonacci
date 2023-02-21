def feb_rec_item(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = feb_rec_item(n-1) + feb_rec_item(n-2)
        return result 
    
def feb_rec(m):
    fibonacci_numbers = []
    for i in range(m+1):
        fibonacci_numbers.append(feb_rec_item(i))
    return fibonacci_numbers





if __name__ == "__main__":
    print(feb_rec_item(19))    # 19th Fibonacci item
    print(feb_rec(19))         # Fibonacci series from 0 to 19 item