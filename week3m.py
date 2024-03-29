"""
Accept a string as input and print PALINDROME if it is a palindrome, and NOT PALINDROME otherwise.
"""
p = input()
if p == p[::-1]:
    print('PALINDROME')
else:
    print(p[::-1])
    print('NOT PALINDROME')
