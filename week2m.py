"""
A test match happened between Team A and Team B.
The scores of the teams in both the innings are given as input in eight lines in the format given below.
The first two lines represent the scores of Team A in the first innings and the next two lines represent the scores
of Team A in the second innings. Likewise, the last four lines represent the scores of Team B in both the innings.

The numbers in 2nd, 4th, 6th, and 8th lines represent the wickets lost by the teams and the numbers in 1st, 3rd, 5th,
and 7th represent the runs scored. For example:

120
10
210
10
115
10
189
10


In the above example, team-A has scored 120 for the loss of 10 wickets in the first innings, and 210 for the loss of 10
wickets in the second innings. Team A plays first and Team B plays second.
Your task is to determine the winner of the match.

*Process to decide the outcome*
Team A wins if and only if the sum of its scores in both the innings is greater than sum of the scores of Team B in both
the innings AND Team B lost all the ten wickets in the second innings. Team B wins if the sum of its scores in both the
innings is greater than sum of the scores of Team A in both the innings.

A match will end in a draw if the sum of scores in the two innings of both the teams are equal OR if Team B did not lose
all the ten wickets in the second innings. If the match ends in a draw, then print DRAW.

Example

120
10
210
10
115
10
189
10

Example output
Team A
120+210>115+189 and Team B lost all 10 wickets in second innings, therefore Team A is the winner of the test match."""

ascore1 = int(input())
awik1 = int(input())
ascore2 = int(input())
awik2 = int(input())
bscore1 = int(input())
bwik1 = int(input())
bscore2 = int(input())
bwik2 = int(input())

asc = ascore1+ascore2
bsc = bscore1+bscore2
if asc > bsc:
    # if ascore1+ascore2>bscore1+bscore2 and bwik1!=0 and bwik2!=0:
    print('Team A')
elif asc == bsc:
    print('DRAW')
else:
    print('Team B')
