f = range(0, 1000)
s = 0
for i in f:
    if i % 3 == 0:
        s = s + i
for j in f:
    if j % 5 == 0 and j % 3 != 0:
        s = s + j
print(s)
