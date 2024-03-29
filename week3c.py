"""
Accept two positive integers a and b as input.
Print the sum of all integers in the range [1000,2000] endpoints inclusive, that are divisible by both a and b.
If you find no number satisfying this condition in the given range, then print 0.
"""
a = int(input())
b = int(input())
sum = 0
for n in range(1000, 2001):
    if n % a == 0 and n % b == 0:
        sum += n
print(sum)
