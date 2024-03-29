"""
Accept a positive integer as input and print the sum of the digits in the number.
"""
n = str(input())
sum = 0
for i in range(len(n)):
    sum += int(n[i])
print(sum)
