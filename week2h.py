"""Consider the following image of a chess-board:

https://www.regencychess.co.uk/blog/wp-content/uploads/2012/05/starting-positon-algebraic.jpg

Accept two positions as input: start and end.
Print YES if a bishop at start can move to end in exactly one move.
Print NO otherwise. Note that a bishop can only move along diagonals."""

s, e = input(), input()
dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
S = dict.index(s[0]) + 1
E = dict.index(e[0]) + 1

if [int(e[1])-int(s[1])] == E-S:
    print('Yes')
else:
    print('No')
