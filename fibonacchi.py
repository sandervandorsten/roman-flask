def fibonacchi(x,y,z):
    fib = [x, y]
    for i in range(z):
        new_val = fib[i] + fib[i+1]
        fib.append(new_val)
    return fib


if __name__ == "__main__":
    output = fibonacchi(1, 2, 6)
    [print(i) for i in output]