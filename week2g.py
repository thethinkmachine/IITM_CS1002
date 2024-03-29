"""
A sequence of five words is called magical if the ith word is a substring of the (i+1)th word
for every i in the range 1≤i<5. Accept a sequence of five words as input, one word on each line.
Print magical if the sequence is magical and non-magical otherwise. Note that str_1 is a substring of str_2 if and 
only if str_1 is present as a sequence of consecutive characters in str_2.
"""
s1,s2,s3,s4,s5=input(),input(),input(),input(),input()
if s1 in s2 and s2 in s3 and s3 in s4 and s4 in s5: # You ABSOLUTELY CAN CHAIN CONDITIONS in an IF-ELSE statement
    print('magical')
else:
    print('non-magical')