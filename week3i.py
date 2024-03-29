"""
Accept a positive integer n as input and print a triangle of zeros for n lines. The ith line should have i zeros.
There shouldn't be any spaces between consecutive zeros. Do not print a space at the end of a line.
"""
n=str(input())
for i in range(0,int(n)+1):
    print('0'*i)