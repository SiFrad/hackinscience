import string
f = list(string.ascii_lowercase)
for i in f:
    for j in f:
        if j != i:
            print(i + j)
