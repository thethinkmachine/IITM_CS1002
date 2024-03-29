"""
Accept an integer between 0 and 24 (endpoints inclusive) and print the time of day.
"""
tod = int(input())
if tod < 0:
    print('INVALID')
elif 0 <= tod <= 5:
    print('NIGHT')
elif 6 <= tod <= 11:
    print('MORNING')
elif 12 <= tod <= 17:
    print('AFTERNOON')
elif 18 <= tod <= 23:
    print('EVENING')
elif tod >= 24:
    print('INVALID')