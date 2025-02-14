#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle edge case for length 0
    if length == 0:
        print("[]")
        return
    
    # Create a list to store Fibonacci numbers
    fibonacci_sequence = []
    
    # Handle the first Fibonacci number (0)
    if length >= 1:
        fibonacci_sequence.append(0)
    
    # Handle the second Fibonacci number (1)
    if length >= 2:
        fibonacci_sequence.append(1)
    
    # Generate the remaining Fibonacci numbers
    for i in range(2, length):
        next_fib = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_fib)
    
    # Print the result
    print(fibonacci_sequence)
