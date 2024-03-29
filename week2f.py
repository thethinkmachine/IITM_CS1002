"""Accept a string as input. If the input string is of odd length, then continue with it. 
If the input string is of even length, make the string of odd length by following the two steps mentioned below:

(1) If the last character is a period (.), then remove it
(2) If the last character is not a period, then add a period (.) to the end of the string

Call this string of odd length word. 
Select a substring made up of three consecutive characters from word such that there are an equal number of characters 
to the left and right of this substring. Print this substring as output.
You can assume that all input strings will be in lower case and will have a length of at least four."""
s = input()
if (len(s) % 2) != 0:                                        # Length of string is odd
    s1 = s
else:                                                        # Length of string is even
    if s[-1] == '.':                                         # if the last character is a '.', remove it.
        s1 = s[:-1]  # <---- Very important
    else:                                                    # if the last character is not a '.', add it.
        s1 = s + '.'  # <---- Very important
medChar = -(-len(s1) // 2) # This is a custom method of rounding off float median values : -(-a//b)
subString = s1[medChar-2:medChar+1]                          # Print 2 characters before the median character
'''Alternatively, you can append individual characters in s1 to generate subString, as shown below:
subString = s1[medChar - 2] + s1[medChar - 1] + s1[medChar]'''
print(subString)
