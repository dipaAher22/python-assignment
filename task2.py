def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1

    if n <= 0:
        return "enter a positive integer"

    elif n == 1:
        fib_sequence.append(a)

    else:
        fib_sequence.append(a)
        fib_sequence.append(b)
        for i in range(2, n):
            next_term = a + b
            fib_sequence.append(next_term)
            a, b = b, next_term

    return fib_sequence

n = int(input("Enter the Fibonacci sequence: "))

result = generate_fibonacci(n)
print("Fibonacci sequence up to {} terms:".format(n))
print(result)
