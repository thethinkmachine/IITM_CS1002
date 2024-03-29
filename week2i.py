"""You have n gold coins with you. You wish to divide this among three of your friends under the following conditions:
(1) All three of them should get a non-zero share.
(2) No two of them should get the same number of coins.
(3) You should not have any coins with you at the end of this sharing process.
The input has four lines. The first line contains the number of coins with you.
The next three lines will have the share given to your three friends.
All inputs shall be non-negative integers.
If the division satisfies these conditions, then print the string FAIR.
If not, print UNFAIR."""

total, s1, s2, s3 = int(input()), int(input()), int(input()), int(input())
if total != 0 and s1 != 0 and s2 != 0 and s3 != 0 and s1 != s2 != s3 and s1 + s2 + s3 == total:
    print('FAIR')
else:
    print('UNFAIR')
