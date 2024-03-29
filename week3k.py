"""
Accept a positive integer nn as input and find all solutions to the equation:
x^2+y^2=z^2

subject to the following constraints:

(1) x, y and z are positive integers
(2) x<y<z<n

Print each solution triplet on one line — x,y,z — with a comma between consecutive integers.
The triplets should be printed in ascending order. If you do not find any solutions satisfying the given constraints,
print the string NO SOLUTION as output.

*Order relation among triplets*

Given two triplets T1=(x1,y1,z1) and T2=(x2,y2,z2), use the following process to compare them:

(1) If x1<x2, then T1<T2

(2) If x1=x2 and y1<y2, then T1<T2

(3) If x1=x2, y1=y2, and z1<z2, then T1<T2
"""

n = int(input())
triples = []
for z in range(1, n):
    for y in range(1, z):
        for x in range(1, y):
            if x ** 2 + y ** 2 == z ** 2:
                triples.append([x, y, z])
                break

if len(triples)==0:
    print('NO SOLUTION')
else:
    triples.sort()
    for a, b, c in triples:
        print(f'{a},{b},{c}')
