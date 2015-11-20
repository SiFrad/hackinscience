import string
f = "abcdefghijklmnopqrstuvwxyz"
for i in range(0,26):
    for j in range(i+1, 26):
        if i != j:
            print(f[i] + f[j])
    
