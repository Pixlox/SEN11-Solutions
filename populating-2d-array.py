def table(m):
    a = []
    for i in range(1, m + 1):
        b = []
        for j in range(1, m + 1):
            b.append(i * j)
        a.append(b)
    return a

m = 5
result = table(m)
for row in result:
    print(row)
