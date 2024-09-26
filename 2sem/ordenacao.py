a = [1, 3, 6, 43, 2, 7, 9]

b = []
for i, j in a:
    if a[i] < a[j]:
        b.append(a[i])
    else:
        b.append(a[i + 1])

print(b)