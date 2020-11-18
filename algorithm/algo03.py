n = 5

factorial = lambda n: n * factorial(n-1) if n > 1 else 1

print(factorial(n))