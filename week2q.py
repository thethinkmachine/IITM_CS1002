"""
EvenOdd is a tech startup. Each employee at the startup is given an employee id which is a unique positive integer.
On one warm Sunday evening, five employees of the company come together for a meeting and sit at a circular table

https://backend.seek.onlinedegree.iitm.ac.in/21t3_cs1002/assets/img/W2GrPA2_exam.png

The employees follow a strange convention. They will continue the meeting only if the following condition is satisfied:
- The sum of the employee-ids of every pair of adjacent employees at the table must be an even number.
- They are so lazy that they won't move around to satisfy the above condition.
If the current seating plan doesn't satisfy the condition, the meeting will be canceled.
You are given the employee-id of all five employees. Your task is to decide if the meeting happened or not.

The input will be five lined, each line containing an integer. The ith line will have the employee-id of Ei.
The output will be a single line containing one of these two strings: YES or NO.
"""

a, b, c, d, e = [int(input()) for i in range(5)]
if (a + b) % 2 == 0 and (b + c) % 2 == 0 and (c + d) % 2 == 0 and (d + e) % 2 == 0:
    print('YES')
else:
    print('NO')
