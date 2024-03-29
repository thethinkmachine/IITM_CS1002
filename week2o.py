"""
Accept four integers as input and write a program to print these integers in non-decreasing order.

The input will be four integers in four lines.
The output should be a single line with all the integers separated by a single space in non-decreasing order.
"""
a, b, c, d = [int(input()) for eachInput in range(4)]  # such a novel way to input numbers
lst=[a,b,c,d]
lst.sort()
print(*lst)