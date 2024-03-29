"""
Accept a positive integer n as input and print the sum of all prime numbers in the range [1,n], endpoints inclusive.
If there are no prime numbers in the given range, then print 0.
"""
# initialize the sum to zero
sump = 0
# read input value from the user
n = int(input())
# iterate over all numbers from 2 to n
for num in range(2, n + 1):
    # assume that the current number is prime
    isPrime = True
    # iterate over all numbers from 2 to num-1
    for i in range(2, num):
        # if num is divisible by i, then it's not a prime number
        if num % i == 0:
            isPrime = False
            break
    # if isPrime is still True, then num is a prime number, so add it to the sum
    if isPrime:
        sump += num
# print the sum of all prime numbers less than or equal to n
print(sump)


