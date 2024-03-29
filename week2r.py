"""
Accept a string as input and print the vowels present in the string in alphabetical order. 
If the string doesn't contain any vowels, then print the string none as output. 
Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the 
output.
"""

a = str(input()).lower()
vowels = ['a', 'e', 'i', 'o', 'u']
seq=''
for i in vowels:
    if i in a:
        seq+=i
    else:
        break
print(seq)
if len(seq)==0:
    print('none')
