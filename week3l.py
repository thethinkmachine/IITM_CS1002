"""
Accept two strings as input and form a new string by removing all characters from the second string which are present in
the first string.  Print this new string as output. You can assume that all input strings will be in lower case.
"""

a = input()
b = input()
for i in a:
    for j in b:
        if i == j:
            b = b.replace(j, '')  # Remember to update the string b.
print(b)
