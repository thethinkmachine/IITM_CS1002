"""
Accept a sequence of positive integers as input and print the maximum number in the sequence.
The input will have n+1 lines, where n denotes the number of terms in the sequence.
The ith line in the input will contain the ith term in the sequence for 1≤i≤n.
The last line of the input will always be the number 0.
Each test case will have at least one term in the sequence.
"""
n = ""
max=0
while n != 0: n= int(input()); max=n if max<=n else print(max)

"""
# ALTERNATE CODE (GENERATED USING GPT)
max_num = 0
while True:
    num = int(input())
    if num == 0:
        break
    if num > max_num:
        max_num = num
print(max_num)
"""
