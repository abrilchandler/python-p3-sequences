#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
        return
    
    first = 0
    second = 1

    fib_sequence = [first]

    for _ in range(length - 1):
        fib_sequence.append(second)
        first, second = second, first + second

    print(fib_sequence)
print_fibonacci(9)