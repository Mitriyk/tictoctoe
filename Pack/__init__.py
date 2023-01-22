n = 50
k = 0
s = ''
for i in range(1, n + 1):
    for j in range(1, i + 1):
        s = s + str(i) + ' '
        k += 1
        if k == n:
            break
    if k == n:
        break
print(s)
