"""Accept two positive integers x and y as input. Print the number of digits in x^y.
You should be able to solve this problem using the concepts covered in week-1."""
a = int(input())
b = int(input())
c = a ** b
d = str(c)
print(len(d))
