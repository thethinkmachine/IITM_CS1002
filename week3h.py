"""
Accept a positive integer n as input and print the first n integers on a line separated by a comma.
"""
n = int(input())
print(*range(1, 1 + n), sep=',')
