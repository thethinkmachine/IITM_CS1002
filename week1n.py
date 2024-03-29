"""Accept a positive integer x as input,
compute the value of this continued fraction and store the result in a variable named cfrac.
Round off your answer to exactly two decimal places. """
x = int(input())
cfrac = (x + 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / x)))))
print(round(cfrac, 2))