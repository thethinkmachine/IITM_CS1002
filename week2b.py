"""Consider the piecewise function given below.

       | x+2 if 0<x<10
f(x)=  | x^2+2 if 10<=x
       | 0 if otherwise

Accept the value of xx as input and print the value of f(x)f(x) as output. Note that both the input and output are real
numbers. Your code should reflect this aspect. That is, both x and f(x) should be float values."""

x = float(input())
if 0 < x < 10:
    print(x + 2)
elif 10 <= x:
    print((x ** 2) + 2)
else:
    print(0)
