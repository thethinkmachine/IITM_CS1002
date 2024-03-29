"""
Accept a positive integer n as input, where n>1. Print PRIME if n is a prime number and NOTPRIME otherwise.
"""
n = int(input())
factors = 0
pstate = True
for i in range(1, n + 1):
    if n % i == 0:
        factors += 1
        if factors > 2:
            pstate = False
print('PRIME' if pstate == True else 'NOTPRIME')
