def fact_gen():
    n = 0
    while True:
        if n == 0:
            yield 1
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            yield factorial
        n += 1

n=int(input("enter value of n"))
factorial_gen = fact_gen()


for i in range(n):
    print(next(factorial_gen))
