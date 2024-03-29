"""
Accept three positive integers as input and check if they form the sides of a right triangle.
Print YES if they form one, and NO if they do not.
The input will have three lines, with one integer on each line.
The output should be a single line containing one of these two strings: YES or NO.
"""
a,b,c=[int(input()) for eachNum in range(3)]
if a**2+b**2==c**2:
    print('YES')
else:
    print('NO')