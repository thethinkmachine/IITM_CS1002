"""
You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger
of the two. If both of them share the same date of birth, then the younger of the two is assumed to be that person whose
name comes first in alphabetical order (names will follow Python's capitalize case format).
"""
# Feed input
nameA = input()
dobA = input()
nameB = input()
dobB = input()

# Perform naive comparison
if dobA[-4:] == dobB[-4:]:  # Same YOB
    if dobA[3:5] == dobB[3:5]:  # Same MOB
        if dobA[0:2] == dobB[0:2]:  # Same DOB
            print(min(nameA, nameB))
        elif dobA[0:2] > dobB[0:2]:  # DOB-A>DOB-B (A is younger)
            print(nameA)
        else:  # DOB-A<DOB-B (B is younger)
            print(nameB)
    elif dobA[3:5] > dobB[3:5]:  # MOB-A>MOB-B (A is younger)
        print(nameA)
    else:  # MOB-A<MOB-B (B is younger)
        print(nameB)
elif dobA[-4:] > dobB[-4:]:  # YOB-A>YOB-B (A is younger)
    print(nameA)
else:  # YOB-A<YOB-B (B is younger)
    print(nameB)
