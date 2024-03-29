"""Accept a non-zero integer as input.
Print positive if it is greater than zero and negative if it is less than zero."""
a = int(input())
if a > 0:
    print('Positive')
elif a == 0:
    print('Unsigned/Neutral')
else:
    print('Negative')