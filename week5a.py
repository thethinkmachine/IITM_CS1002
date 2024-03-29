def min(a):
    mini = a[0]
    for i in range(len(a)):
        if a[i] < mini:
            mini = a[i]
    return mini


def sort(a):
    b = []
    while len(a) > 0:
        mini = a
