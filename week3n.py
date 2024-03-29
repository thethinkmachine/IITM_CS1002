a, b = [int(input()) for i in range(2)]
af = []
for i in range(a):
    for j in range(a+1):
        if i * j == a:
            af.append([i, j])
print(af)