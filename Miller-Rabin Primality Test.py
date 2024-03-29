import random

# get input from user
n = int(input("Enter an integer: "))
k = int(input("Enter the number of iterations: "))

# check if n is prime using Miller-Rabin test
if n < 2:
    print(n, "is not prime")
elif n == 2 or n == 3:
    print(n, "is prime")
elif n % 2 == 0:
    print(n, "is not prime")
else:
    # write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # repeat k times
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            print("It is not prime")
            break
    else:
        print("It probably is a prime number")
